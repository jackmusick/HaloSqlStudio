declare module "bifrost" {
  import type { ReactNode } from "react";

  export type Theme = "light" | "dark";

  export interface BifrostContextValue {
    baseUrl: string;
    token: string;
    orgScope: string | null;
    appId: string | null;
    authedFetch: typeof fetch;
    logout: () => void;
    theme: Theme;
    setTheme: (theme: Theme) => void;
    toggleTheme: () => void;
    supportsTheme: boolean;
  }

  export function useBifrostContext(): BifrostContextValue;

  export interface BifrostProviderProps {
    baseUrl: string;
    token: string;
    orgScope?: string | null;
    appId?: string | null;
    fetchImpl?: typeof fetch;
    onLogout?: () => void;
    supportsTheme?: boolean;
    theme?: Theme;
    onThemeChange?: (theme: Theme) => void;
    children: ReactNode;
  }

  export function BifrostProvider(props: BifrostProviderProps): JSX.Element;
  export function BifrostHeader(props: {
    title: string;
    logo?: string | null;
    action?: ReactNode;
    className?: string;
  }): JSX.Element;

  export interface UseWorkflowState<T> {
    data: T | null;
    loading: boolean;
    error: Error | null;
    run: (input?: Record<string, unknown>) => Promise<T>;
  }

  export function useWorkflow<T = unknown>(workflowRef: string): UseWorkflowState<T>;

  export interface TableDocument {
    id: string;
    data: Record<string, unknown>;
    created_at?: string;
    updated_at?: string;
  }

  export const tables: {
    get(table: string, id: string, scope?: string): Promise<TableDocument | null>;
    insert(table: string, data: Record<string, unknown>, scope?: string): Promise<TableDocument>;
    upsert(table: string, item: { id: string; data: Record<string, unknown> }, scope?: string): Promise<TableDocument>;
    update(table: string, id: string, data: Record<string, unknown>, scope?: string): Promise<TableDocument | null>;
    delete(table: string, id: string | string[], scope?: string): Promise<unknown>;
    query(
      table: string,
      query?: Record<string, unknown>,
      scope?: string,
    ): Promise<{ documents: TableDocument[]; total: number }>;
  };
}
