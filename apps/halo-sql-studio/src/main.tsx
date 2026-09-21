import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { BifrostProvider } from "bifrost";

import App from "./App";
import "./index.css";

// Deployed: the platform injects this app's bootstrap (mount node, basename,
// per-viewer token, org). It keys the bootstrap by THIS entry's `m` nonce in a
// registry, so a fast navigation between two apps can't make our still-loading
// entry read the OTHER app's bootstrap (Codex #9). Read our own nonce from this
// module's URL and prefer the registry; fall back to the legacy single object
// (older hosts) and finally to a local #root for `npm run dev`.
const __m = new URL(import.meta.url).searchParams.get("m");
const boot =
  (__m && window.__BIFROST_APPS__ && window.__BIFROST_APPS__[__m]) ||
  window.__BIFROST_APP__;
const mountEl = boot?.mountEl ?? document.getElementById("root")!;
const basename = boot?.basename ?? "/";
const baseUrl = boot?.baseUrl ?? import.meta.env.VITE_BIFROST_API_URL ?? window.location.origin;
const token = boot?.token ?? import.meta.env.VITE_BIFROST_TOKEN ?? "";
// Precedence (boot over VITE env) is locked by client/src/lib/app-sdk/dev-bootstrap.test.ts
const orgScope = boot?.orgScope ?? import.meta.env.VITE_BIFROST_ORG_ID ?? null;
// This app's id, so useWorkflow scopes path refs to THIS install's workflow.
const appId = boot?.appId ?? import.meta.env.VITE_BIFROST_APP_ID ?? null;
// Platform theme, so the app starts in sync. supportsTheme is ON by default:
// the scaffold ships Tailwind + the shadcn `.dark` token layer, so the app DOES
// respond to theme — which makes BifrostHeader show the light/dark toggle.
const theme = boot?.theme ?? "light";

const root = createRoot(mountEl);
// Let the platform tear this root down on navigation (no leak).
boot?.registerUnmount?.(() => root.unmount());

root.render(
  <StrictMode>
    <BifrostProvider baseUrl={baseUrl} token={token} orgScope={orgScope} appId={appId} theme={theme} supportsTheme onLogout={boot?.onLogout}>
      <BrowserRouter basename={basename}>
        <App />
      </BrowserRouter>
    </BifrostProvider>
  </StrictMode>,
);
