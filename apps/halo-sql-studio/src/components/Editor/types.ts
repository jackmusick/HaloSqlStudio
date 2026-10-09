export interface QueryResult {
    rows: unknown[];
    columns?: Array<{ name: string }>;
    rowCount?: number;
    executionTime?: number;
    hasError?: boolean;
    error?: string;
}

export interface Report {
    id: string;
    name: string;
    sql: string;
}
