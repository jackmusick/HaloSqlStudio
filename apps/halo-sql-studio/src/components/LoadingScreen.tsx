import { Loader2 } from "lucide-react";

export function LoadingScreen({ message }: { message: string }) {
    return (
        <div className="flex h-full items-center justify-center bg-background">
            <div className="flex flex-col items-center gap-3 text-center">
                <Loader2 className="h-8 w-8 animate-spin text-primary" aria-hidden="true" />
                <h1 className="text-lg font-semibold">Halo SQL Studio</h1>
                <p className="text-sm text-muted-foreground">{message}</p>
            </div>
        </div>
    );
}
