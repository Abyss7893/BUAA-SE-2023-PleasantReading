<!-- 网页的主页的中间内容部分 -->
<template>
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