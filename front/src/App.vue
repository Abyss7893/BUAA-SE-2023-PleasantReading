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
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  text-decoration: none;
}
</style>

<style lang="scss">
// 引入 css
@import url(./assets/css/public.css);
</style>