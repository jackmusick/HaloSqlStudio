import { useCallback, useState } from "react";
import { tables, useWorkflow } from "bifrost";

import type { ApiResponse, QueryResult, ReportInfo, TableInfo } from "@/services/api/types";
import { useConfigStore } from "@/stores/configStore";
import { useSqlRuntimeStore } from "@/stores/runtimeStore";

interface SchemaTable {
    name: string;
    columns: Array<{
        name: string;
        data_type: string;
        ordinal_position: number;
    }>;
}

async function readSchemaTables(): Promise<SchemaTable[]> {
    const rows: SchemaTable[] = [];
    let offset = 0;
    while (true) {
        const result = await tables.query("halo_sql_schema_cache", {
            order_by: "created_at",
            order_dir: "asc",
            limit: 1000,
            offset,
        });
        rows.push(...result.documents.map((document) => document.data as unknown as SchemaTable));
        if (result.documents.length < 1000) return rows;
        offset += result.documents.length;
    }
}

function toQueryResult(response: ApiResponse, executionTime: number): QueryResult {
    if (response?.report?.load_error) {
        return { columns: [], rows: [], executionTime, error: response.report.load_error, hasError: true };
    }
    if (response?.available_columns && response?.report?.rows) {
        return {
            columns: response.available_columns,
            rows: response.report.rows,
            rowCount: response.report.rows.length,
            executionTime,
            hasError: false,
        };
    }
    return { columns: [], rows: [], executionTime, error: "Unexpected response format", hasError: true };
}

export function useApi() {
    const executeWorkflow = useWorkflow<ApiResponse>("functions/halo_sql_studio.py::execute_query");
    const reportsWorkflow = useWorkflow<ApiResponse>("functions/halo_sql_studio.py::list_reports");
    const saveWorkflow = useWorkflow<{ id: string }>("functions/halo_sql_studio.py::save_report");
    const refreshWorkflow = useWorkflow("functions/halo_sql_studio.py::refresh_cache");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const executeQuery = useCallback(async (sql: string): Promise<QueryResult> => {
        setIsLoading(true);
        setError(null);
        const started = performance.now();
        try {
            const response = await executeWorkflow.run({
                sql,
                agent_id: useConfigStore.getState().agentId,
            });
            return toQueryResult(response, Math.round(performance.now() - started));
        } catch (reason) {
            const message = reason instanceof Error ? reason.message : "Failed to execute query";
            setError(message);
            throw reason;
        } finally {
            setIsLoading(false);
        }
    }, [executeWorkflow.run]);

    const getTables = useCallback(async (): Promise<TableInfo[]> => {
        let schemaTables = await readSchemaTables();
        if (!schemaTables.length) {
            useSqlRuntimeStore.getState().setCacheRefreshType("schema");
            try {
                await refreshWorkflow.run({ cache_type: "schema", reason: "cache_miss" });
                schemaTables = await readSchemaTables();
            } finally {
                useSqlRuntimeStore.getState().setCacheRefreshType(null);
            }
        }

        return schemaTables
            .map((table) => ({
                name: table.name,
                columns: table.columns
                    .sort((a, b) => a.ordinal_position - b.ordinal_position)
                    .map((column, index) => ({
                        id: index,
                        name: column.name,
                        data_type: column.data_type,
                        data_type_group: "unknown",
                    })),
            }))
            .sort((a, b) => a.name.localeCompare(b.name));
    }, [refreshWorkflow.run]);

    const getReports = useCallback(async (): Promise<ReportInfo[]> => {
        const response = await reportsWorkflow.run();
        const result = toQueryResult(response, 0);
        if (result.hasError) throw new Error(result.error || "Failed to load reports");
        const groups = new Map<string, { id: string; name: string; sql: string }[]>();
        for (const row of result.rows) {
            const group = row.Group || "Uncategorized";
            const reports = groups.get(group) ?? [];
            reports.push({ id: String(row.Id), name: row.Name || "Unnamed Report", sql: row.SQL || "" });
            groups.set(group, reports);
        }
        return Array.from(groups.entries())
            .map(([name, reports]) => ({ name, reports: reports.sort((a, b) => a.name.localeCompare(b.name)) }))
            .sort((a, b) => a.name.localeCompare(b.name));
    }, [reportsWorkflow.run]);

    const createOrUpdateReport = useCallback(async (reportData: {
        sql: string;
        name: string;
        description?: string;
        id?: string;
    }): Promise<{ id: string }> => saveWorkflow.run({
        sql: reportData.sql,
        name: reportData.name,
        description: reportData.description ?? "",
        report_id: reportData.id ? Number(reportData.id) : null,
    }), [saveWorkflow.run]);

    const updateReport = useCallback(
        (reportId: string, sql: string) => createOrUpdateReport({ id: reportId, sql, name: "" }).then(() => undefined),
        [createOrUpdateReport],
    );

    return {
        executeQuery,
        getTables,
        getReports,
        createOrUpdateReport,
        updateReport,
        isLoading,
        error,
        clearError: () => setError(null),
    };
}
