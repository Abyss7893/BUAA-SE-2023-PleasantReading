<!-- home页面 -->
<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
                                        <LoginComponent /> -->
  <div id="app">
    <RouterView></RouterView>
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
    if (sessionStorage.getItem('store')) {
      this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(sessionStorage.getItem('store'))));
    }

    //在页面刷新时将vuex里的信息保存到sessionStorage里
    window.addEventListener('beforeunload', () => {
      sessionStorage.setItem('store', JSON.stringify(this.$store.state));
    });
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  text-decoration: none;
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