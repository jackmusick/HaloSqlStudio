import { create } from "zustand";

export interface HaloConfig {
    tenant: string;
    authServer: string;
    resourceServer: string;
    clientId: string;
    redirectUri: string;
}

interface ConfigState {
    config: HaloConfig;
    agentId: number | null;
    agentName: string;
    isLoaded: boolean;
    isConfigured: boolean;
    setEnvironment: (resourceServer: string, agentId: number, agentName: string) => void;
    setConfig: (updates: Partial<HaloConfig>) => void;
    resetConfig: () => void;
    setLoaded: (loaded: boolean) => void;
    generateRedirectUri: () => string;
}

const emptyConfig: HaloConfig = {
    tenant: "",
    authServer: "",
    resourceServer: "",
    clientId: "",
    redirectUri: "",
};

export const useConfigStore = create<ConfigState>((set) => ({
    config: emptyConfig,
    agentId: null,
    agentName: "",
    isLoaded: true,
    isConfigured: true,
    setEnvironment: (resourceServer, agentId, agentName) =>
        set({ config: { ...emptyConfig, resourceServer }, agentId, agentName, isLoaded: true, isConfigured: true }),
    setConfig: (updates) => set((state) => ({ config: { ...state.config, ...updates } })),
    resetConfig: () => undefined,
    setLoaded: (isLoaded) => set({ isLoaded }),
    generateRedirectUri: () => "",
}));
