module.exports = {
  purge: ["./src/**/*.svelte", "./src/*.html"],
  variants: {},
  theme: {
    extend: {
      fontFamily: {
        serif: '"GFS Didot", ui-serif',
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
};
