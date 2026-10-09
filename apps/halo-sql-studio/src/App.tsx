import React, { useCallback, useEffect, useRef, useState } from "react";
import { tables, useBifrostContext, useWorkflow } from "bifrost";

import { CacheRefreshOverlay } from "@/components/CacheRefreshOverlay";
import { LoadingScreen } from "@/components/LoadingScreen";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import Index from "@/pages/Index";
import { useConfigStore } from "@/stores/configStore";
import { useSqlRuntimeStore } from "@/stores/runtimeStore";

class ErrorBoundary extends React.Component<
    { children: React.ReactNode },
    { hasError: boolean }
> {
    state = { hasError: false };

    static getDerivedStateFromError() {
        return { hasError: true };
    }

    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
        console.error("Halo SQL Studio render error", error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return (
                <div className="flex h-full items-center justify-center bg-background p-6 text-center">
                    <div>
                        <h1 className="text-xl font-semibold">Unable to render Halo SQL Studio</h1>
                        <button
                            className="mt-4 border border-border px-4 py-2 text-sm hover:bg-accent"
                            onClick={() => window.location.reload()}
                        >
                            Reload
                        </button>
                    </div>
                </div>
            );
        }
        return this.props.children;
    }
}

function BifrostBootstrap({ children }: { children: React.ReactNode }) {
    const { authedFetch } = useBifrostContext();
    const refresh = useWorkflow("functions/halo_sql_studio.py::refresh_cache");
    const refreshRef = useRef(refresh.run);
    refreshRef.current = refresh.run;
    const inFlightRef = useRef<Promise<void> | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [ready, setReady] = useState(false);

    const initialize = useCallback(() => {
        setError(null);
        setReady(false);
        const request = (async () => {
            const meResponse = await authedFetch("/api/auth/me");
            if (!meResponse.ok) throw new Error("Unable to identify the calling Bifrost user");
            const me = await meResponse.json() as { email?: string };
            const email = String(me.email ?? "").trim().toLowerCase();
            if (!email) throw new Error("The calling Bifrost user does not have an email address");

            const readCache = async () => {
                const [agents, environment] = await Promise.all([
                    tables.query("halo_sql_agents", { where: { email_lower: email }, limit: 2 }),
                    tables.get("halo_sql_cache_state", "environment"),
                ]);
                return {
                    agent: agents.documents[0]?.data as { id?: number; name?: string } | undefined,
                    haloBaseUrl: String(environment?.data?.halo_base_url ?? ""),
                };
            };

            let cached = await readCache();
            if (!cached.agent || !cached.haloBaseUrl) {
                useSqlRuntimeStore.getState().setCacheRefreshType("agents");
                try {
                    await refreshRef.current({ cache_type: "agents", reason: "cache_miss" });
                    cached = await readCache();
                } finally {
                    useSqlRuntimeStore.getState().setCacheRefreshType(null);
                }
            }
            if (!cached.agent?.id) throw new Error(`No Halo agent matches Bifrost user ${email}`);
            if (!cached.haloBaseUrl) throw new Error("The cached Halo environment is unavailable");
            useConfigStore.getState().setEnvironment(
                cached.haloBaseUrl,
                Number(cached.agent.id),
                String(cached.agent.name ?? email),
            );
        })()
            .then(() => {
                setReady(true);
            })
            .catch((reason) => {
                setError(reason instanceof Error ? reason.message : String(reason));
            })
            .finally(() => {
                inFlightRef.current = null;
            });
        inFlightRef.current = request;
        return request;
    }, [authedFetch]);

    useEffect(() => {
        if (!inFlightRef.current) void initialize();
    }, [initialize]);

    if (error) {
        return (
            <div className="flex h-full items-center justify-center bg-background p-6 text-center">
                <div className="max-w-xl">
                    <h1 className="text-xl font-semibold">Unable to initialize Halo SQL Studio</h1>
                    <p className="mt-2 text-sm text-muted-foreground">{error}</p>
                    <button
                        className="mt-5 border border-border px-4 py-2 text-sm hover:bg-accent"
                        onClick={() => void initialize()}
                    >
                        Retry connection
                    </button>
                </div>
            </div>
        );
    }

    if (!ready) return <LoadingScreen message="Connecting to Halo reporting..." />;
    return children;
}

export default function App() {
    return (
        <ErrorBoundary>
            <TooltipProvider>
                <BifrostBootstrap>
                    <Index />
                    <CacheRefreshOverlay />
                </BifrostBootstrap>
                <Toaster />
            </TooltipProvider>
        </ErrorBoundary>
    );
}
