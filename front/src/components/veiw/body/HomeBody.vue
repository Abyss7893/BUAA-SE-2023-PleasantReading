<!-- 网页的主页的中间内容部分 -->
<template>
  <div class="box-center">
    <div class="novel-body">
      <div class="category-component-wrapper">
        <CategoryComponent />
        <!-- <p>dwdwdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd</p> -->
      </div>
      <el-divider direction="vertical"></el-divider>
      <div class="recommend-component-wrapper">
        <RecommendComponent />
      </div>
    </div>
  </div>
</template>
<script>
import CategoryComponent from "./CategoryComponent.vue";
import RecommendComponent from "./RecommendComponent.vue";
export default {
  name: "HomeBody",
  components: {
    CategoryComponent,
    RecommendComponent,
  },
};
</script>

<style scoped>
.el-divider--vertical {
  display: inline-block;
  width: 1px;
  height: 100%;
  margin: 0 8px;
  vertical-align: middle;
  position: relative;
}
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
  flex-grow: 1;
}
</style>