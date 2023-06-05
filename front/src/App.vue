<!-- home页面 -->
<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
                                                                                                                                                                                                                                                                                                      <LoginComponent /> -->
  <div id="app">
    <RouterView :key="$route.fullPath" prefetch></RouterView>
  </div>
</template>

<script>
// import HomeComponent from './components/home/Home.vue';
// import LoginComponent from './components/login/LoginComponent.vue';
// import RegisterComponent from './components/login/RegisterComponent.vue';
// import "assets/css/public.css";
export default {
  name: "App",
  components: {
    // LoginComponent,
    // HomeComponent,
    // LoginComponent,
    // RegisterComponent,
  },
  created() {
    //在页面加载时读取sessionStorage里的状态信息
    if (localStorage.getItem('store')) {
      this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(localStorage.getItem('store'))));
    }
    //在页面刷新时将vuex里的信息保存到sessionStorage里
    window.addEventListener('beforeunload', () => {
      localStorage.setItem('store', JSON.stringify(this.$store.state));
    });
  },
  unmounted() {
    localStorage.removeItem('token')
  },
};
</script>

<style>
@font-face {
  font-style: normal;
  font-family: 'Harmony_Regular';
  /*引入HarmonyOS_Sans_SC，目录别搞错*/
  src: url('~assets/fonts/HarmonyOS_Sans_SC_Regular.ttf') format('truetype');
}

* {
  margin: 0;
  padding: 0;
  text-decoration: none;
  outline: none;
  /* -moz-user-select: none; */
  /* 火狐国产版需要 */
  /* -webkit-user-select: none; */
  /* Safari、Chrome 等需要 */
  /* -ms-user-select: none; */
  /* IE10+ 需要 */
  /* user-select: none; */
  /* 标准语法，其他浏览器需要 */

}

body {
  font-family: 'Harmony_Regular', sans-serif !important;
  width: 100%;
  min-width: 1200px;
}

a,
button {
  transition: color .3s, background-color .3s;
}

.float {
  float: left;
}

.flex {
  display: flex;
}

.clear {
  clear: both;
}

a {
  color: #262626;
  outline: none;
  text-decoration: none;
}

li,
ol,
ul {
  list-style: none outside none;
}

/* dark模式 */
body.dark #app>div.basic-bcg,
body.dark #app>div.basic-bcg a,
body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd>a>span,
body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd>a>svg>path,
body.dark #app>div.basic-bcg>div.center-box>div.text>div.info,
body.dark #app>div.basic-bcg>div.center-box>div.text>div.info svg path,
body.dark #app>div.basic-bcg>div.center-box>div.chapter-control a,
body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(4)>div.panel.comments>div>ul>li {
  transition: color .1s, fill .1s;
  color: #666;
  fill: #666;
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>div a {
  color: white;
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div>div>ul>li {
  border-bottom: 1px solid rgba(255, 255, 255, .1);
}

body.dark #app>div:nth-child(7)>footer {
  display: none;
}

body.dark .placeholder,
body.dark #fixheight {
  background: url('~assets/imgs/readerbcg/dark/base.png');
  z-index: -100;
}

body.dark #app>div.basic-bcg>div.center-box>div.chapter-control a:hover,
body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd:hover a span,
body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd:hover svg path {
  fill: #ed4259;
  color: #ed4259;
  background: hsla(0, 0%, 100%, .03);
}

body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd,
body.dark #app>div.basic-bcg>div.center-box>div.text,
body.dark #app>div.basic-bcg>div.center-box>div.chapter-control,
body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>span {
  border: 1px solid rgba(255, 255, 255, .1);
}

body.dark #app>div.basic-bcg>div.reader-menu.float>dl>dd.act {
  border-right: none;
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li.font-list>span.act {
  border: 1px solid #ed4259;
  color: #ed4259;
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>cite {
  border: 1px solid rgba(255, 255, 255, .1);
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li span,
body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>cite,
body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>cite>span svg path {
  transition: color .1s, fill .1s;
  fill: #a6a6a6;
  color: #a6a6a6;
  background-color: rgba(255, 255, 255, 0.05);
}

body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>cite span:hover,
body.dark #app>div.basic-bcg>div.reader-menu.float>div:nth-child(3)>div>div>ul>li>cite>span:hover svg path {
  fill: #ed4259;
  color: #ed4259;
}
</style>

<style lang="scss">
// 引入 css
@import url(./assets/css/public.css);
</style>