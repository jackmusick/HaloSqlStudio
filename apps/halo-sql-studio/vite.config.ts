import { execFileSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { dirname, join, parse } from "node:path";

import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Tokenless local dev — three sources, in order:
//   1. process env (the CLI exported BIFROST_API_URL/BIFROST_ACCESS_TOKEN), then
//   2. the nearest .env walking UP from this app dir (password-grant `login`
//      writes one), then
//   3. the CLI credential store via `bifrost auth token` — device-code login
//      stores the token in the OS keyring / ~/.bifrost/credentials.json (NOT a
//      .env), so without this the normal login path leaves `npm run dev`
//      tokenless (R7-P2-f).
// Deployed, window.__BIFROST_APP__ supplies these instead and main.tsx prefers it.
function readBifrostEnv() {
  const out = {
    url: process.env.BIFROST_API_URL || "",
    token: process.env.BIFROST_ACCESS_TOKEN || "",
  };
  let dir = process.cwd();
  while (!(out.url && out.token)) {
    const envPath = join(dir, ".env");
    if (existsSync(envPath)) {
      for (const line of readFileSync(envPath, "utf8").split("\n")) {
        const m = line.match(/^\s*(BIFROST_API_URL|BIFROST_ACCESS_TOKEN)\s*=\s*(.*)\s*$/);
        if (m) {
          const v = m[2].replace(/^["']|["']$/g, "");
          if (m[1] === "BIFROST_API_URL" && !out.url) out.url = v;
          if (m[1] === "BIFROST_ACCESS_TOKEN" && !out.token) out.token = v;
        }
      }
    }
    const parent = dirname(dir);
    if (parent === dir || dir === parse(dir).root) break;
    dir = parent;
  }
  // Fall back to the CLI credential store (keyring / credentials.json).
  if (!out.token) {
    try {
      const args = ["auth", "token"];
      if (out.url) args.push("--url", out.url);
      const raw = execFileSync("bifrost", args, {
        encoding: "utf8",
        stdio: ["ignore", "pipe", "ignore"],
      });
      const creds = JSON.parse(raw);
      if (creds.access_token) out.token = creds.access_token;
      if (creds.api_url && !out.url) out.url = creds.api_url;
    } catch {
      // CLI absent / not logged in — leave tokenless; main.tsx surfaces the
      // unauthenticated state rather than crashing the dev server.
    }
  }
  return out;
}

export default defineConfig(({ command }) => {
  const env = readBifrostEnv();
  // SECURITY: the dev token is injected ONLY for `vite` (serve / `npm run dev`),
  // never for `vite build`. Baking BIFROST_ACCESS_TOKEN into the production
  // bundle via `define` would ship a usable credential to every app user
  // (Codex R6-P1-c). In a deployed build the token comes from
  // window.__BIFROST_APP__ at runtime (per viewer); the bundle stays tokenless.
  const define =
    command === "serve"
      ? {
          "import.meta.env.VITE_BIFROST_API_URL": JSON.stringify(env.url),
          "import.meta.env.VITE_BIFROST_TOKEN": JSON.stringify(env.token),
          "import.meta.env.VITE_BIFROST_APP_ID": JSON.stringify(process.env.VITE_BIFROST_APP_ID || ""),
          "import.meta.env.VITE_BIFROST_ORG_ID": JSON.stringify(process.env.VITE_BIFROST_ORG_ID || null),
        }
      : {};
  return {
    plugins: [react()],
    define,
    // `@/` → src, so shadcn component source (which imports `@/lib/utils` and
    // `@/components/ui/*`) resolves the same as in the shadcn docs.
    resolve: { alias: { "@": join(process.cwd(), "src") } },
    server: { allowedHosts: ["development"] },
    build: { chunkSizeWarningLimit: 2500 },
  };
});
