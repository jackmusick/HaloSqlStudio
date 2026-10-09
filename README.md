# Halo SQL Studio

Halo SQL Studio is a Bifrost Solution for exploring HaloPSA reporting tables,
executing SQL through Halo's reporting API, and creating or updating Halo
reports. It replaces the legacy standalone browser app: Bifrost owns
authentication, the Halo connection, and Solution deployment.

## Install from this repository

Log in to the Bifrost instance where the Solution should be installed, then
install the repository-managed Solution:

```bash
bifrost solution install-repo https://github.com/jackmusick/HaloSqlStudio.git --ref main
```

Repository installation makes Git the Solution's writer. Updates run through
the platform's managed Git lifecycle after repository changes; do not use a
separate browser deployment or copy the legacy app's OAuth settings into the
client.

## Access and Halo connection

The app, its workflows, and its cache tables are restricted to the `Service
Managers` role. Ensure that role exists and assign it to the people who should
use SQL Studio before installation.

Configure the Solution's declared `HaloPSA` connection in Bifrost. Its mapping
must contain the API resource `base_url`, such as
`https://your-tenant.halopsa.com/api`, and the Halo OAuth client-credentials
settings for that tenant. The portable manifest creates the client-credentials
skeleton and required base URL field, but does not guess tenant-specific token
endpoints or include credentials. OAuth tokens stay in Bifrost; the browser
does not receive or store them.

`HaloPSA` is a shared Bifrost integration name. A Solution install reuses an
existing connection without overwriting it, so an integration administrator
must approve its use and grant the Halo client only the reporting permissions
needed for this Solution. API calls run with those shared integration
privileges. The caller's Bifrost email only resolves `$agentid` for SQL
substitution; it does not create a per-user Halo authentication session.

After the connection is configured, run the first cache refresh:

```bash
bifrost workflows execute functions/halo_sql_studio.py::refresh_cache \
  --params '{"cache_type":"all","reason":"initial"}'
```

The locator resolves against workflows visible to the caller. If the same
Solution is installed in multiple scopes, use `bifrost workflows list`, select
the matching workflow UUID, and execute that UUID with `--org <target-org>` as
needed.

The Solution then refreshes the same caches daily at 3:23 AM America/New_York.
Reports and query results remain live and are not cached.

## Architecture

- `apps/halo-sql-studio`: Bifrost React app with Monaco and AG Grid.
- `functions/halo_sql_studio.py`: portable query, report, and cache workflows.
- `modules/halopsa`: vendored HaloPSA client plus the reporting extension.
- `halo_sql_agents`: caller-to-Halo-agent cache.
- `halo_sql_schema_cache`: table and column cache for the explorer and completion.
- `halo_sql_cache_state`: refresh metadata and the non-secret Halo base URL.

## Local development

Run local development from the Solution root with a CLI that matches the
selected Bifrost instance:

```bash
bifrost solution start halo-sql-studio
```

`solution start` installs the selected instance's Bifrost web SDK transiently.
Deployed builds receive that SDK from the serving platform, so the app's
`package.json` deliberately does not pin an instance URL. If multiple installs
share this slug, pass the intended install explicitly with
`--solution <install-id>`.

## Verification

```bash
python3 -m pytest -q
cd apps/halo-sql-studio
npm run build
```

## Release verification

This repository publishes the Solution source. Existing installations are not
redeployed by this source replacement alone. `npm audit --json` reports zero
advisories for the committed frontend lockfile. A credentialed non-production
installation and browser acceptance pass remain required before claiming live
Halo execution or production release readiness.
