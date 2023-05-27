<!-- 网页的主页的中间内容部分 -->
<template>
  <head-and-foot>
    <div class="box-center">
      <!-- <div class="novel-body">
        <div class="category-component-wrapper">
          <CategoryComponent />
        </div>
        <div class="recommend-component-wrapper"> -->
      <RankComponent />
      <!-- </div> -->
      <!-- </div> -->
    </div>
  </head-and-foot>
</template>
  <script>
// import CategoryComponent from "../body/CategoryComponent.vue";
import RankComponent from "./RankComponent.vue";
import HeadAndFoot from "../HeadAndFoot.vue";
export default {
  name: "HomeBody",
  components: {
    // CategoryComponent,
    RankComponent,
    HeadAndFoot,
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