<!-- home页面 -->
<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
                                                                <LoginComponent /> -->
  <div id="app">
    <RouterView :key="$route.fullPath"></RouterView>
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

body {
  width: 100%;
  min-width: 1200px;
}
</style>

<style lang="scss">
// 引入 css
@import url(./assets/css/public.css);
</style>