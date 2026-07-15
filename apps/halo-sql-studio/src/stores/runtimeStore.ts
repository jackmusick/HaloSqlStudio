import { create } from "zustand";

interface SqlRuntimeState {
    cacheRefreshType: string | null;
    setCacheRefreshType: (cacheType: string | null) => void;
}

export const useSqlRuntimeStore = create<SqlRuntimeState>((set) => ({
    cacheRefreshType: null,
    setCacheRefreshType: (cacheRefreshType) => set({ cacheRefreshType }),
}));
