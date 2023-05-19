<!-- home页面 -->
<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
                                                                  <LoginComponent /> -->
  <div>
    <head-top @login-dialog="dialogVisible = true"></head-top>
    <LoginComponent v-if="dialogVisible" @close-dialog="dialogVisible = false"></LoginComponent>
    <NovelHomepage />
    <HeadAndFoot>
      <HomeBody />
    </HeadAndFoot>
  </div>
</template>
<script>
import HeadAndFoot from "../veiw/HeadAndFoot.vue";
import HomeBody from "../veiw/body/HomeBody.vue";
// import AboutFoot from "../veiw/about/AboutFoot.vue";

import LoginComponent from "./login/LoginComponent.vue";

// import NovelHomepage from "../home/home2.vue";
// import CategoryComponent from "../veiw/content/CategoryComponent.vue";
// import RecommendComponent from "../veiw/content/RecommendComponent.vue";
export default {
  name: "HomeComponent",
  components: {
    LoginComponent,
    HeadAndFoot,
    HomeBody,
    // AboutFoot,
    // NovelHomepage
    // CategoryComponent,
    // RecommendComponent,
  },
  data() {
    return {
      dialogVisible: false // 控制 Login 组件的显示与隐藏
    };
  }
};
</script>