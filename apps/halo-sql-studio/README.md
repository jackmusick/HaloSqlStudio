# halo-sql-studio — a Bifrost standalone_v2 app

## Local dev (no token pasting)

You only need to be logged in with the CLI once — `npm run dev` reads the token
`bifrost login` already wrote (from the environment, or the nearest `.env` up
the directory tree). So from your logged-in solution workspace:

    npm install     # resolves `bifrost` from https://bifrost.gocovi.com
    npm run dev     # http://localhost:5173 — already authenticated

(If you run `npm run dev` somewhere the CLI's `.env` isn't reachable, copy
`.env.example` to `.env` and set the two BIFROST_* values.)

## Deploy

The platform builds the app server-side and serves it at `/apps/halo-sql-studio`:

    bifrost deploy
