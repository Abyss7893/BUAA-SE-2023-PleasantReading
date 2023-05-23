<!-- 网页的主页的中间内容部分 -->
<template>
  <div>
    <ElAffix>
      <WebHead />
    </ElAffix>

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

    <FootComponents />
  </div>
</template>
  
  <script>
import WebHead from "../head/WebHead.vue";
import FootComponents from "../foot/WebFoot.vue";
import { ElAffix } from "element-plus";
// import StartComponent from "./StartComponent.vue";
import CategoryComponent from "./CategoryComponent.vue";
import RecommendComponent from "./RecommendComponent.vue";
export default {
  name: "HomeBody",
  components: {
    CategoryComponent,
    RecommendComponent,
    // StartComponent,
    WebHead,
    FootComponents,

    ElAffix,
  },
};
</script>
  
  <style scoped>
.box-center {
  margin-left: auto;
  margin-right: auto;
  width: 1200px;
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