<template>
  <!-- <div class="novel-sidebar"> -->
  <div class="category float">
    <div class="float" v-for="(title, titleIndex) in categories.titles" :key="titleIndex">
      <div class="category-title">{{ title }}</div>
      <ul class="float">
        <li class="float" v-for="(category, index) in categories.content[title]" :key="index"
          :ref="`categoryItem_${titleIndex}_${index}`" @click="selectCategory(titleIndex, index)">
          {{ category }}
        </li>
        <div class="sub-category"
          v-if="titleIndex == 0 && (('category' in this.$route.query && this.categories.content['分类'].includes(this.$route.query.category)) || ('sub' in this.$route.query) && subCategories)">
          <a :class="subCategory === this.$route.query.sub ? 'act' : ''" @click="selectsubCategory(subCategory)"
            v-for="(subCategory, subindex) in subCategories" :key="subindex" :ref="`sub_${subCategory}`">{{
              subCategory }}</a>
        </div>
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
          '分类': [
            "全部",
            "武侠",
            "现实",
            "军事",
            "历史",
            "科幻",
            "悬疑",
            "轻小说",
            "都市",
          ],
          '二级分类': {
            "武侠": ['传统武侠', '武侠幻想', '国术无双', '古武未来', '武侠同人'],
            "现实": ['时代叙事', '家庭伦理', '女性题材', '青年故事', '社会悬疑', '人间百态'],
            "军事": ['军旅生涯', '军事战争', '战争幻想', '抗战烽火', '谍战特工'],
            "历史": ['架空历史', '秦汉三国', '上古先秦', '历史传记', '两晋隋唐', '五代十国', '两宋元明', '清史民国', '外国历史', '民间传说'],
            "科幻": ['古武机甲', '未来世界', '星际文明', '超级科技', '时空穿梭', '进化变异', '末世危机'],
            "悬疑": ['诡秘悬疑', '奇妙世界', '侦探推理', '探险生存', '古今传奇'],
            "轻小说": ['原生幻想', '恋爱日常', '衍生同人', '搞笑吐槽'],
            '都市': ['都市生活', '娱乐明星', '都市异能', '商战职场', '青春校园'],
          },
          '状态': ["全部", "连载", "完结"],
          '属性': ["全部", "免费", "VIP"],
          '字数': [
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
      nowCategories: [0, 0, 0, 0],
    };
  },
  computed: {
    subCategories() {
      if ('category' in this.$route.query)
        return this.categories.content['二级分类'][this.$route.query.category]
      else if ('sub' in this.$route.query) {
        for (let cat in this.categories.content['二级分类']) {
          if (this.categories.content['二级分类'][cat].includes(this.$route.query.sub))
            return this.categories.content['二级分类'][cat]
        }
      }
      return null
    },
  },
  mounted() {
    this.setRefs();
    this.nowCategories[0] = this.categories.content['分类'].indexOf(this.$route.query.category)
    this.nowCategories[1] = this.categories.content['状态'].indexOf(this.$route.query.status)
    if ('vip' in this.$route.query)
      this.nowCategories[2] = this.$route.query.vip === "true" ? 2 : 1
    this.nowCategories[3] = this.categories.content['字数'].indexOf(this.categories.content['字数'][this.$route.query.range])
    this.nowCategories.forEach((content, idx) => {
      if (content == -1)
        content = 0
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
      var Option = {};
      for (let key in this.$route.query) {
        if (key === 'sub')
          continue
        Option[key] = this.$route.query[key];
      }
      if (titleIndex == 0) {
        if (index === 0) {
          if ("category" in Option)
            delete Option.category
        }
        else
          Option["category"] = this.categories.content['分类'][index]
      }
      if (titleIndex == 1) {
        if (index === 2) Option["status"] = "完结";
        if (index === 1) Option["status"] = "连载";
        if (index === 0) {
          if ("status" in Option)
            delete Option.status
        }
      }
      if (titleIndex == 2) {
        if (index === 2) Option["vip"] = true;
        if (index === 1) Option["vip"] = false;
        if (index === 0) {
          if ("vip" in Option)
            delete Option.vip
        }
      }

      if (titleIndex == 3) {
        if (index > 0) Option["range"] = index;
        else if ("range" in Option) {
          delete Option.range
        }
      }
      // Option["data"] = new Date().getTime();
      this.$router.push({ name: "Child", query: Option });
    },
    selectsubCategory(subCategory) {
      var Option = {};
      for (let key in this.$route.query) {
        Option[key] = this.$route.query[key];
      }
      Option['sub'] = subCategory
      this.$router.push({ name: "Child", query: Option });
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
  transition: background-color .3s;
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

.category .sub-category {
  background: #fef0f0;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  clear: both;
  margin-bottom: 10px;
  padding: 5px 8px;
  float: left;
}

.category .sub-category a {
  word-wrap: break-word;
  float: left;
  font: 12px/28px PingFangSC-Regular, -apple-system, Simsun;
  margin-right: 2px;
  padding: 0 4px;
  border-radius: 5px;
  line-height: 24px;
}

.category .sub-category a:hover {
  background-color: rgb(245, 108, 108);
  color: white
}

.category .sub-category a.act {
  background-color: rgb(245, 108, 108);
  color: white
}
</style>
