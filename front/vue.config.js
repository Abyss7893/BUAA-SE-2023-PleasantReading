const { defineConfig } = require('@vue/cli-service')
const path = require('path');
function resolve(dir) {
  return path.join(__dirname, dir);
}
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    config.resolve.alias
      .set("@", resolve("src"))
      .set("assets", resolve("src/assets"))
      .set("components", resolve("src/components"))
      .set("views", resolve("src/components/views"))
      .set("css", resolve("src/assets/css"))
      // .set("base", resolve("baseConfig"))
      .set("public", resolve("public"));
  },
})
