import { lazy, Suspense, useCallback, useEffect, useRef, useState } from "react";
import { BifrostHeader } from "bifrost";
import { GripVertical } from "lucide-react";

import { Explorer } from "@/components/Explorer";

const Editor = lazy(() =>
    import("@/components/Editor").then((module) => ({ default: module.Editor })),
);

export default function Index() {
    const [explorerWidth, setExplorerWidth] = useState(() => {
        const saved = localStorage.getItem("explorerWidth");
        return saved ? parseInt(saved, 10) : 320;
    });
    const isResizingRef = useRef(false);
    const startXRef = useRef(0);
    const startWidthRef = useRef(0);

    const handleMouseDown = useCallback((event: React.MouseEvent) => {
        isResizingRef.current = true;
        startXRef.current = event.clientX;
        startWidthRef.current = explorerWidth;
        document.body.style.cursor = "col-resize";
        document.body.style.userSelect = "none";
    }, [explorerWidth]);

    const handleMouseMove = useCallback((event: MouseEvent) => {
        if (!isResizingRef.current) return;
        const width = Math.max(220, Math.min(600, startWidthRef.current + event.clientX - startXRef.current));
        setExplorerWidth(width);
        localStorage.setItem("explorerWidth", String(width));
    }, []);

    const handleMouseUp = useCallback(() => {
        isResizingRef.current = false;
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
    }, []);

    useEffect(() => {
        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
        return () => {
            document.removeEventListener("mousemove", handleMouseMove);
            document.removeEventListener("mouseup", handleMouseUp);
        };
    }, [handleMouseMove, handleMouseUp]);

    return (
        <div className="flex h-full min-h-0 flex-col bg-background text-foreground">
            <BifrostHeader title="Halo SQL Studio" />
            <div className="flex min-h-0 flex-1">
                <aside className="relative flex-shrink-0" style={{ width: explorerWidth }}>
                    <Explorer />
                </aside>
                <div
                    className="relative flex w-px flex-shrink-0 cursor-col-resize items-center justify-center bg-border"
                    onMouseDown={handleMouseDown}
                    title="Drag to resize Explorer"
                >
                    <div className="z-10 flex h-5 w-3 items-center justify-center border bg-border">
                        <GripVertical className="h-3 w-3 text-foreground" />
                    </div>
                </div>
                <main className="flex min-w-0 flex-1 flex-col">
                    <Suspense
                        fallback={
                            <div className="flex h-full items-center justify-center text-sm text-muted-foreground">
                                Loading SQL editor...
                            </div>
                        }
                    >
                        <Editor />
                    </Suspense>
                </main>
            </div>
        </div>
    );
}
