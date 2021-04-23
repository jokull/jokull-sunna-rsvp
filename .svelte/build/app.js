import { ssr } from '@sveltejs/kit/ssr';
import root from './generated/root.svelte';
import { set_paths } from './runtime/paths.js';
import { set_prerendering } from './runtime/env.js';
import * as user_hooks from "./hooks.js";

const template = ({ head, body }) => "<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"utf-8\" />\n    <meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\" />\n    <meta name=\"theme-color\" content=\"#333333\" />\n\n    " + head + "\n\n    <link rel=\"stylesheet\" href=\"global.css\" />\n    <link rel=\"manifest\" href=\"manifest.json\" crossorigin=\"use-credentials\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"favicon.png\" />\n    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" />\n    <link\n      href=\"https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,700;1,400;1,700&display=swap\"\n      rel=\"stylesheet\"\n    />\n  </head>\n  <body>\n    <!-- The application will be rendered inside this element,\n\t     because `src/client.js` references it -->\n    <div id=\"svelte\">" + body + "</div>\n  </body>\n</html>\n";

let options = null;

// allow paths to be overridden in svelte-kit preview
// and in prerendering
export function init(settings) {
	set_paths(settings.paths);
	set_prerendering(settings.prerendering || false);

	options = {
		amp: false,
		dev: false,
		entry: {
			file: "/./_app/start-6d5dc625.js",
			css: ["/./_app/assets/start-230d6437.css"],
			js: ["/./_app/start-6d5dc625.js","/./_app/chunks/vendor-57fbb124.js"]
		},
		fetched: undefined,
		get_component_path: id => "/./_app/" + entry_lookup[id],
		get_stack: error => String(error), // for security
		handle_error: error => {
			console.error(error.stack);
			error.stack = options.get_stack(error);
		},
		hooks: get_hooks(user_hooks),
		hydrate: true,
		initiator: undefined,
		load_component,
		manifest,
		paths: settings.paths,
		read: settings.read,
		root,
		router: true,
		ssr: true,
		target: "#svelte",
		template
	};
}

const d = decodeURIComponent;
const empty = () => ({});

const manifest = {
	assets: [{"file":"background-tile.png","size":57434,"type":"image/png"},{"file":"branch.png","size":40483,"type":"image/png"},{"file":"favicon.png","size":29542,"type":"image/png"},{"file":"global.css","size":584,"type":"text/css"},{"file":"leaves.png","size":247207,"type":"image/png"},{"file":"logo-192.png","size":63029,"type":"image/png"},{"file":"logo-512.png","size":410991,"type":"image/png"},{"file":"manifest.json","size":358,"type":"application/json"},{"file":"opengraph.png","size":970857,"type":"image/png"},{"file":"paper.jpg","size":190007,"type":"image/jpeg"}],
	layout: "src/routes/$layout.svelte",
	error: ".svelte/build/components/error.svelte",
	routes: [
		{
						type: 'page',
						pattern: /^\/$/,
						params: empty,
						a: ["src/routes/$layout.svelte", "src/routes/index.svelte"],
						b: [".svelte/build/components/error.svelte"]
					},
		{
						type: 'page',
						pattern: /^\/responses\/?$/,
						params: empty,
						a: ["src/routes/$layout.svelte", "src/routes/responses.svelte"],
						b: [".svelte/build/components/error.svelte"]
					}
	]
};

// this looks redundant, but the indirection allows us to access
// named imports without triggering Rollup's missing import detection
const get_hooks = hooks => ({
	getContext: hooks.getContext || (() => ({})),
	getSession: hooks.getSession || (() => ({})),
	handle: hooks.handle || (({ request, render }) => render(request))
});

const module_lookup = {
	"src/routes/$layout.svelte": () => import("../../src/routes/$layout.svelte"),".svelte/build/components/error.svelte": () => import("./components/error.svelte"),"src/routes/index.svelte": () => import("../../src/routes/index.svelte"),"src/routes/responses.svelte": () => import("../../src/routes/responses.svelte")
};

const metadata_lookup = {"src/routes/$layout.svelte":{"entry":"/./_app/pages/$layout.svelte-040c1e8e.js","css":["/./_app/assets/pages/$layout.svelte-84b7f494.css"],"js":["/./_app/pages/$layout.svelte-040c1e8e.js","/./_app/chunks/vendor-57fbb124.js"],"styles":null},".svelte/build/components/error.svelte":{"entry":"/./_app/error.svelte-3d07235c.js","css":[],"js":["/./_app/error.svelte-3d07235c.js","/./_app/chunks/vendor-57fbb124.js"],"styles":null},"src/routes/index.svelte":{"entry":"/./_app/pages/index.svelte-36a98090.js","css":[],"js":["/./_app/pages/index.svelte-36a98090.js","/./_app/chunks/vendor-57fbb124.js"],"styles":null},"src/routes/responses.svelte":{"entry":"/./_app/pages/responses.svelte-75c9e814.js","css":[],"js":["/./_app/pages/responses.svelte-75c9e814.js","/./_app/chunks/vendor-57fbb124.js"],"styles":null}};

async function load_component(file) {
	return {
		module: await module_lookup[file](),
		...metadata_lookup[file]
	};
}

init({ paths: {"base":"","assets":"/."} });

export function render(request, {
	prerender
} = {}) {
	const host = request.headers["host"];
	return ssr({ ...request, host }, options, { prerender });
}