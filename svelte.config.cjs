const sveltePreprocess = require("svelte-preprocess");
const static = require("@sveltejs/adapter-static");
const pkg = require("./package.json");

/** @type {import('@sveltejs/kit').Config} */
module.exports = {
  preprocess: [
    sveltePreprocess({
      defaults: {
        style: "postcss",
      },
      postcss: true,
    }),
  ],
  kit: {
    adapter: static(),

    // hydrate the <div id="svelte"> element in src/app.html
    target: "#svelte",

    prerender: {
      pages: ["*"],
    },

    vite: {
      ssr: {
        noExternal: Object.keys(pkg.dependencies || {}),
      },
    },
  },
};
