<template>
  <!-- <div class="novel-sidebar"> -->
  <div class="flex">
    <div class="category">
      <h3>分类</h3>
      <ul>
        <li
          v-for="(category, index) in categories"
          :key="index"
          :class="{ active: category.active }"
          @mouseover="highlightCategory(index)"
          @mouseout="removeHighlight(index)"
          @click="changeRoute(category.route, category.filter)"
        >
          {{ category.name }}
        </li>
      </ul>
      <!-- </div> -->
    </div>
    <el-divider direction="vertical"></el-divider>
  </div>
</template>

<script>
export default {
  name: "CategoryComponent",
  data() {
    return {
      categories: [
        {
          name: "玄幻",
          route: "/fantasy",
          filter: { genre: "玄幻" },
          active: false,
        },
        {
          name: "修真",
          route: "/martial",
          filter: { genre: "修真" },
          active: false,
        },
        {
          name: "都市",
          route: "/city",
          filter: { genre: "都市" },
          active: false,
        },
        {
          name: "历史",
          route: "/history",
          filter: { genre: "历史" },
          active: false,
        },
      ],
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
      this.categories[index].active = true;
    },
    removeHighlight(index) {
      this.categories[index].active = false;
    },
  },
};
</script>

<style scoped>
.category {
  width: 200px;

}
.category li.active {
  background-color: #f39c12;
  color: #fff;
  cursor: pointer;
}

.category li:hover {
  background-color: #3498db;
  color: #fff;
  cursor: pointer;
}
.left-sider {
  
}
.el-divider--vertical {
  display: inline-block;
  width: 1px;
  height: 100%;
  margin: 0 8px;
  vertical-align: middle;
  position: relative;
  float: right;
}
</style>
