<!-- 网页的主页的中间内容部分 -->
<template>
  <div class="this-body">
    <start-component @hide="hideStartComponent" />
    <LoadingPage v-if="showLoading" />
  <!-- <div>
      <WebHead style="margin: 0,position:fixed;" />
      <div>
        <div class="box-center">
          <div class="novel-body">
            <div class="category-component-wrapper">
              <CategoryComponent />
            </div>
            <div class="recommend-component-wrapper">
              <RecommendComponent />
            </div>
          </div>
        </div>
      </div>
      <FootComponents />
                                </div> -->
  </div>
</template>
<script>
// import WebHead from "../head/WebHead.vue";
// import FootComponents from "../foot/WebFoot.vue";
// import { ElAffix } from "element-plus";
import StartComponent from "./StartComponent.vue";
// // import {   ,stopp } from "@/api/sakura";
// import CategoryComponent from "./CategoryComponent.vue";
// import RecommendComponent from "./RecommendComponent.vue";
import LoadingPage from "@/components/page/LoadingPage.vue";
export default {
  name: "HomeBody",
  components: {
    // CategoryComponent,
    // RecommendComponent,
    StartComponent,
    LoadingPage,
    // WebHead,
    // FootComponents,
    // ElAffix,
  },
  data() {
    return {
      // showHeadAndFoot: false,
      showLoading: false,
    };
  },
  methods: {
    hideStartComponent() {
      setTimeout(() => {
        this.showLoading = true;
      }, 50);
    },
  },
};
</script>

<style scoped>
.box-center {
  margin-left: auto;
  margin-right: auto;
  width: 1200px;
  min-height: 70vh;
}

.category-component-wrapper {
  width: 200px;
  float: left;
  /* flex-grow: 0; */
}

.recommend-component-wrapper {
  float: left;
  margin-left: 20px;
  flex-grow: 1;
}
</style>