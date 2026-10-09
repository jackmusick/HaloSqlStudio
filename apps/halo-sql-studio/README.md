# halo-sql-studio — Bifrost Solution app

## Local development

From the Solution root, use the Bifrost CLI to start the app and local
workflows on one origin:

```bash
bifrost solution start halo-sql-studio
```

The command supplies the selected instance and token to Vite and installs its
web SDK transiently. The deployed platform injects the same SDK during its
build, so `package.json` must not declare a Bifrost SDK URL. After one
`solution start`, `npm run dev` can be used for app-only iteration with the
selected CLI profile.

## Deploy

This app is deployed only through the repository-managed Solution lifecycle.
Do not deploy it as a separate static app or run a local deployment against a
Git-managed install.
