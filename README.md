# Halo SQL Studio

Halo SQL Studio is a Bifrost Solution for exploring HaloPSA reporting tables,
executing SQL through Halo's reporting API, and creating or updating Halo
reports.

## Architecture

- `apps/halo-sql-studio`: standalone Bifrost React app with Monaco and AG Grid.
- `functions/halo_sql_studio.py`: portable query, report, and cache workflows.
- `modules/halopsa`: vendored HaloPSA integration client plus reporting extension.
- `halo_sql_agents`: daily Halo agent cache used to map the Bifrost caller by email.
- `halo_sql_schema_cache`: daily table/column cache used by the explorer and SQL completion.
- `halo_sql_cache_state`: daily refresh metadata plus the non-secret Halo base URL.
- Reports and query results remain live and are not cached.

The app does not store Halo OAuth tokens or configuration in the browser. All
Halo calls resolve the Solution's declared `HaloPSA` connection through Bifrost.
Startup identity and environment details are read directly from Bifrost and the
Solution cache, so opening the app does not enqueue a workflow.

## Local development

```bash
bifrost solution start halo-sql-studio \
  --host 0.0.0.0 \
  --port 4183 \
  --public-url http://development:4183
```

## Verification

```bash
cd apps/halo-sql-studio
npm run build

cd ../..
/home/jack/.local/share/pipx/venvs/bifrost/bin/python -m pytest -q
```
