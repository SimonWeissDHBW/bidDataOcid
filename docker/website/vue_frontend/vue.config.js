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
    proxy: 'http://localhost/cell_towers',
  },
  headers: {
    "Access-Control-Allow-Origin": "*",
 }
})
