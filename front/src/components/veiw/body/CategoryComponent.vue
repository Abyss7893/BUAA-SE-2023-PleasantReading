<template>
  <!-- <div class="novel-sidebar"> -->
  <div class="category float">
    <div
      class="float"
      v-for="(title, titleIndex) in categories.titles"
      :key="titleIndex"
    >
      <div class="category-title">{{ title }}</div>
      <ul class="float">
        <li
          class="float"
          v-for="(category, index) in categories.content[title]"
          :key="index"
          :ref="`categoryItem_${titleIndex}_${index}`"
          @click="selectCategory(titleIndex, index)"
        >
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
        titles: ["分类", "状态", "属性", "字数"],
        content: {
          分类: [
            "全部",
            "玄幻",
            "奇幻",
            "武侠",
            "仙侠",
            "都市",
            "现实",
            "军事",
            "历史",
            "游戏",
            "体育",
            "科幻",
            "诸天无限",
            "悬疑",
            "轻小说",
            "短篇",
          ],
          状态: ["全部", "连载", "完本"],
          属性: ["全部", "免费", "VIP"],
          字数: [
            "全部",
            "30万字以下",
            "30-50万字",
            "50-100万字",
            "100-200万字",
            "200万字以上",
          ],
        },
      },
      categoryItems: [], // 存储 li 元素数组的引用
    };
  },
  mounted() {
    this.setRefs();
    let categoriesContent = this.$store.state.categoriesIndex;
    // console.log(categoriesContent)
    categoriesContent.forEach((content, idx) => {
      let elm = this.categoryItems[idx][content];
      elm.style.backgroundColor = "#f56c6c";
      elm.style.color = "white";
    });
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
    // 设置 refs
    setRefs() {
      this.categories.titles.forEach((title, titleIndex) => {
        let items = this.categories.content[title];
        let refs = [];
        items.forEach((item, index) => {
          refs.push(this.$refs[`categoryItem_${titleIndex}_${index}`][0]);
        });
        this.categoryItems.push(refs);
      });
    },
    // 点击事件处理函数
    selectCategory(titleIndex, index) {
      let categoriesContent = this.$store.state.categoriesIndex;
      // console.log(categoriesContent)
      // 设置选中的 li 元素的样式
      this.categoryItems[titleIndex][
        categoriesContent[titleIndex]
      ].style.backgroundColor = "";
      this.categoryItems[titleIndex][
        categoriesContent[titleIndex]
      ].style.color = "";
      this.categoryItems[titleIndex][index].style.backgroundColor = "#f56c6c";
      this.categoryItems[titleIndex][index].style.color = "white";

      var Option=this.$route.query;
      // if (!("category" in this.$route.query))
      //   Option = {
      //     category: "null",
      //     property: "null",
      //     status: "null",
      //     wordCount: "null",
      //     sort: "null",
      //   };
      // else Option = this.$route.query;
      if (titleIndex == 1) {
        if (index === 2) Option["property"] = "完结";
        if (index === 1) Option["property"] = "连载";
        if (index === 0) Option["property"] = "null";
      }
      if (titleIndex == 2) {
        if (index === 2) Option["property"] = "VIP";
        if (index === 1) Option["property"] = "FREE";
        if (index === 0) Option["property"] = "null";
      }

      if (titleIndex == 3) {
        if (index > 0) Option["wordCount"] = index;
        else Option["wordCount"] = "null";
      }
      // Option["data"] = new Date().getTime();
      console.log(Option);
      this.$router.push({ name: "Child", query: Option });
      // this.$router.push({
      //   path: `/allbook/${Option.category}/${Option.property}/${Option.status}/${Option.wordCount}/${Option.sort}`,
      // });
      // 更新 $store 中的 categoriesIndex 值
      this.$store.commit("changeCategoriesIndex", {
        title: titleIndex,
        index: index,
      });
    },
  },
};
</script>

<style scoped>
.category {
  width: 200px;
  min-width: 200px;
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
  background-color: #fef0f0;
  cursor: pointer;
}
</style>
