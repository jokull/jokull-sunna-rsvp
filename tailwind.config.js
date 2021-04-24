module.exports = {
  purge: ["./src/**/*.svelte", "./src/*.html"],
  variants: {},
  theme: {
    extend: {
      fontFamily: {
        serif: '"Crimson Pro", ui-serif, serif',
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
};
