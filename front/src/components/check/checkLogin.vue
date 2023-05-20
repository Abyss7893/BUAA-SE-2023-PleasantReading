<template>
  <div v-if="isLogin">
    <slot></slot>
    <!-- <h1 v-else>  -->
  </div>
  <!-- <el-button type="info" @click="changeLoginState">点击切换登录状态</el-button> -->
</template>

<script>
import store from "@/store";
export default {
  // ...
  computed: {
    isLogin() {
      return store.state.isLogin;
    },
  },

  created() {
    if (!store.state.isLogin) {
      this.$router.push("/login");
    }
  },
  methods: {
    changeLoginState() {
      store.commit("changeLoginState");
    },
    // setVIP() {
    //   store.commit("setVIP");
    // },
  },
  // ...
};
</script>

<style>
</style>