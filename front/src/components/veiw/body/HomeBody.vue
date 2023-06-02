<!-- 网页的主页的中间内容部分 -->
<template>
  <div style="display: flex; flex-direction: column">
    <start-component  @hide="hideStartComponent" />
    <div >
      <!-- <ElAffix> -->
      <WebHead style="margin: 0,position:fixed;" />
      <!-- </ElAffix> -->
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
    </div>
  </div>
</template>
<script>
import WebHead from "../head/WebHead.vue";
import FootComponents from "../foot/WebFoot.vue";
// import { ElAffix } from "element-plus";
import StartComponent from "./StartComponent.vue";
import CategoryComponent from "./CategoryComponent.vue";
import RecommendComponent from "./RecommendComponent.vue";
export default {
  name: "HomeBody",
  components: {
    CategoryComponent,
    RecommendComponent,
    StartComponent,
    WebHead,
    FootComponents,

    // ElAffix,
  },
  data() {
    return {
      showHeadAndFoot: false,
      showStartComponent:true
    };
  },
  methods: {
    // handleScroll(event) {
    //   // 获取滚动容器的scrollTop属性，表示滚动的距离
    //   const scrollTop = event.target.scrollTop;

    //   // 定义允许向下滚动的距离
    //   const allowedScrollDistance = 1.06 * window.innerHeight; // 100为示例值，您可以根据实际情况调整

    //   // 判断是否允许向上滚动
    //   if (scrollTop > allowedScrollDistance) {
    //     // 如果滚动距离超过允许的距离，禁止向上滚动
    //     event.target.scrollTop = allowedScrollDistance;
    //     console.log("scrollTop: " + scrollTop);
    //   }
    // },
    hideStartComponent() {
      setTimeout(() => {
        this.showHeadAndFoot = true;
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