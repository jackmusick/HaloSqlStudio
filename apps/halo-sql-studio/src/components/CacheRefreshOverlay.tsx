import { Database, Loader2 } from "lucide-react";

import { useSqlRuntimeStore } from "@/stores/runtimeStore";

export function CacheRefreshOverlay() {
    const cacheRefreshType = useSqlRuntimeStore((state) => state.cacheRefreshType);
    if (!cacheRefreshType) return null;

    return (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-background/95 p-6">
            <div className="flex max-w-md flex-col items-center gap-4 text-center">
                <div className="relative">
                    <Database className="h-10 w-10 text-primary" />
                    <Loader2 className="absolute -right-3 -top-3 h-5 w-5 animate-spin text-primary" />
                </div>
                <h2 className="text-lg font-semibold">Refreshing {cacheRefreshType} cache...</h2>
                <p className="text-sm text-muted-foreground">Please wait. This window will continue automatically.</p>
            </div>
        </div>
    );
}
