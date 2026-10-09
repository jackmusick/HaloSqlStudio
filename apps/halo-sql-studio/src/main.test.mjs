import assert from "node:assert/strict";
import test from "node:test";

import { build } from "esbuild";

async function loadEntry() {
  const result = await build({
    entryPoints: [new URL("./main.tsx", import.meta.url).pathname],
    bundle: true,
    format: "esm",
    platform: "browser",
    jsx: "automatic",
    write: false,
    define: { "import.meta.env.DEV": "false" },
    plugins: [
      {
        name: "mount-test-stubs",
        setup(pluginBuild) {
          pluginBuild.onResolve({ filter: /^(react|react\/jsx-runtime|react-dom\/client|react-router-dom|bifrost)$/ }, (args) => ({
            path: args.path,
            namespace: "mount-test-stub",
          }));
          pluginBuild.onResolve({ filter: /^\.\/App$/ }, () => ({
            path: "app",
            namespace: "mount-test-stub",
          }));
          pluginBuild.onResolve({ filter: /\.css$/ }, () => ({
            path: "style",
            namespace: "mount-test-stub",
          }));
          pluginBuild.onLoad({ filter: /.*/, namespace: "mount-test-stub" }, (args) => {
            const modules = {
              react: "const React = { createElement: (type, props, ...children) => ({ type, props: { ...props, children: children.length <= 1 ? children[0] : children } }) }; export default React; export const StrictMode = Symbol('StrictMode');",
              "react/jsx-runtime": "export const jsx = (type, props) => ({ type, props }); export const jsxs = jsx;",
              "react-dom/client": "export const createRoot = (element) => ({ render: (tree) => globalThis.__roots.push({ element, tree }), unmount: () => globalThis.__unmounts.push(element) });",
              "react-router-dom": "export const BrowserRouter = Symbol('BrowserRouter');",
              bifrost: "export const BifrostProvider = Symbol('BifrostProvider');",
              app: "export default function App() { return null; }",
              style: "",
            };
            return { contents: modules[args.path], loader: "js" };
          });
        },
      },
    ],
  });
  return import(`data:text/javascript;base64,${Buffer.from(result.outputFiles[0].contents).toString("base64")}`);
}

function providerProps(tree) {
  return tree.props.children.props;
}

test("mount-v1 creates independent roots and forwards each host bootstrap", async () => {
  globalThis.__roots = [];
  globalThis.__unmounts = [];
  globalThis.window = { __BIFROST_APP_MODULES__: new Map() };

  const entry = await loadEntry();
  const firstMount = { id: "first" };
  const firstBootstrap = {
    basename: "/apps/halo-sql-studio",
    baseUrl: "https://first.example",
    token: "first-token",
    orgScope: "first-org",
    appId: "first-app",
    solutionId: "first-solution",
    theme: "light",
    onLogout: () => undefined,
  };
  const stopFirst = entry.mount(firstMount, firstBootstrap);

  assert.equal(globalThis.__roots.length, 1);
  assert.equal(globalThis.__roots[0].element, firstMount);
  const firstProvider = providerProps(globalThis.__roots[0].tree);
  assert.equal(firstProvider.baseUrl, firstBootstrap.baseUrl);
  assert.equal(firstProvider.token, firstBootstrap.token);
  assert.equal(firstProvider.orgScope, firstBootstrap.orgScope);
  assert.equal(firstProvider.appId, firstBootstrap.appId);
  assert.equal(firstProvider.solutionId, firstBootstrap.solutionId);
  assert.equal(firstProvider.supportsTheme, true);

  stopFirst();
  const secondMount = { id: "second" };
  const secondBootstrap = { ...firstBootstrap, baseUrl: "https://second.example", token: "second-token" };
  const stopSecond = entry.mount(secondMount, secondBootstrap);

  assert.deepEqual(globalThis.__unmounts, [firstMount]);
  assert.equal(globalThis.__roots.length, 2);
  assert.equal(globalThis.__roots[1].element, secondMount);
  assert.equal(providerProps(globalThis.__roots[1].tree).baseUrl, secondBootstrap.baseUrl);
  assert.equal(providerProps(globalThis.__roots[1].tree).token, secondBootstrap.token);
  assert.ok(
    [...globalThis.window.__BIFROST_APP_MODULES__.values()].some(
      (module) => module.mount === entry.mount,
    ),
  );

  stopSecond();
  assert.deepEqual(globalThis.__unmounts, [firstMount, secondMount]);
});
