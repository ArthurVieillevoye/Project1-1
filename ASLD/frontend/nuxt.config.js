export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "ASLD",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  srcDir: "./",

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    "~/assets/scss/main.scss",
    "~assets/materialicons/css/materialdesignicons.min.css",
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [{ src: "~/plugins/decision-tree.js", mode: "all" }],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: ["~/components", "~/components/Cards", "~/components/Shared"],

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    "@nuxt/postcss8",
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: ["@nuxtjs/axios"],

  // tailwindcss: { exposeConfig: true, configPath: "./tailwind.config.js" },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
};
