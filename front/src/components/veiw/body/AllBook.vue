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
          <RecommendComponent :Option="Option" />
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
  data() {
    return {
      Option: {},
    };
  },
  name: "HomeBody",
  components: {
    CategoryComponent,
    RecommendComponent,
    // StartComponent,
    WebHead,
    FootComponents,

    ElAffix,
  },
  computed: {},
  created() {
    for (let key in this.$route.query) {
      if (key === "property") {
        if (this.$route.query[key] === "VIP") this.Option["vip"] = "true";
        else if (this.$route.query[key] === "FREE")
          this.Option["vip"] = "false";
        else this.Option['vip'] = "";
      }
      if (key === "wordCount")this.Option['range'] = this.$route.query[key];
      this.Option[key] = this.$route.query[key];
      console.log(key, this.Option[key]);
    }
    // console.log({
    //   category: this.category,
    //   vip: this.property == "VIP",
    //   status: this.status,
    //   range: this.wordCount,
    //   order: this.sort,
    // });
    // this.naviLoccation = document
    //   .querySelector(`li[navi-id="${id}"]`)
    //   .getBoundingClientRect();
    // this.$store.commit("changeNaviLoc", id);
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