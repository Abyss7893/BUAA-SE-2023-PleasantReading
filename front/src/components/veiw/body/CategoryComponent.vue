<template>
  <!-- <div class="novel-sidebar"> -->
  <div class="category float">
    <div class="type-filter float">
      <div class="category-title">分类</div>
      <ul class="float">
        <li class="float" v-for="(category, index) in categories.type" :key="index" @mouseover="highlightCategory(index)"
          @mouseout="removeHighlight(index)">
          {{ category }}
        </li>
      </ul>
    </div>
    <div class="status-filter float">
      <div class="category-title">状态</div>
      <ul class="float">
        <li class="float" v-for="(category, index) in categories.status" :key="index"
          @mouseover="highlightCategory(index)" @mouseout="removeHighlight(index)">
          {{ category }}
        </li>
      </ul>
    </div>
    <div class="vip-filter float">
      <div class="category-title">属性</div>
      <ul class="float">
        <li class="float" v-for="(category, index) in categories.vip" :key="index" @mouseover="highlightCategory(index)"
          @mouseout="removeHighlight(index)">
          {{ category }}
        </li>
      </ul>
    </div>
    <div class="count-filter float">
      <div class="category-title">字数</div>
      <ul class="float">
        <li class="float" v-for="(category, index) in categories.count" :key="index" @mouseover="highlightCategory(index)"
          @mouseout="removeHighlight(index)">
          {{ category }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategoryComponent",
  data() {
    return {
      categories: {
        type: ["全部", "玄幻", "奇幻", "武侠", "仙侠", "都市", "现实", "军事", "历史", "游戏", "体育", "科幻", "诸天无限", "悬疑", "轻小说", "短篇"],
        status: ["全部", "连载", "完本"],
        vip: ["全部", "免费", "VIP"],
        count: ["全部", "30万字以下", "30-50万字", "50-100万字", "100-200万字", "200万字以上"],
      },
    };
  },
  methods: {
    changeRoute(route, filter) {
      this.$router.push({
        path: route,
        query: filter,
      });
      // 将对应标签的 active 属性设为 true
      let index = this.categories.findIndex(
        (category) => category.route === route
      );
      this.categories.forEach((category, idx) => {
        category.active = index === idx;
      });
    },
    highlightCategory(index) {
      // this.categories[index].active = true;
      console.log(this.categories[index])
    },
    removeHighlight(index) {
      // this.categories[index].active = false;
      console.log(this.categories[index])
    },
  },
};
</script>

<style scoped>
.category {
  width: 200px;
  margin-top: 41px;
}

.category ul {
  padding-bottom: 4px;
  margin-bottom: 15px;
  width: 200px;
  border-bottom: 1px solid #ebebeb;
}

.category ul li {
  border-radius: 5px;
  list-style: none;
  padding: 0 4px;
  margin: 0 8px 8px 0;
  height: 20px;
  font: 12px/20px PingFangSC-Regular, -apple-system, Simsun;
  text-align: center;
}



.category .category-title {
  margin-bottom: 15px;
  font-size: 15px;
  font: 15px/20px PingFangSC-Regular, -apple-system, Simsun;
  font-weight: bold;
}

.category li:hover {
  background-color: #f56c6c;
  color: #fff;
  cursor: pointer;
}
</style>
