const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'quasar'
  ],

  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false
    }
  },
  devServer: {
    port: 3000,
    ws: true,
    changeOrigin: true,
    proxy: 'http://localhost',
  },
  headers: {
    "Access-Control-Allow-Origin": "*",
 }
})
