const { defineConfig } = require('@vue/cli-service')
const path = require('path');
function resolve(dir) {
  return path.join(__dirname, dir);
}
module.exports = defineConfig({
  devServer: {// 环境配置
    // host: 'localhost',
    // port: 8088,
    open: true, //配置自动启动浏览器
  },
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
