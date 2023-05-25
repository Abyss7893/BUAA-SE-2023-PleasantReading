<template>
  <div>
    <div class="block-col-2">
      <el-dropdown
        @command="handleCommand"
        style="line-height: 150%"
        trigger="click"
      >
        <span class="demonstration">
          {{ cod
          }}<el-icon class="el-icon--right">
            <arrow-down /><i class="arrow-down"></i
          ></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu class="rank-dropdown-menu">
            <!-- 按照评分降序 -->
            <el-dropdown-item command="1">按评分降序</el-dropdown-item>
            <!-- 按照评分升序 -->
            <el-dropdown-item command="2">按评分升序</el-dropdown-item>
            <!-- 按照字数降序 -->
            <el-dropdown-item command="3">按字数降序</el-dropdown-item>
            <!-- 按照字数升序 -->
            <el-dropdown-item command="4">按字数升序</el-dropdown-item>
            <el-dropdown-item command="5">按收藏降序</el-dropdown-item>
            <el-dropdown-item command="6">按收藏升序</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
    <book-gallery ref="child" :Option="Option"></book-gallery>
  </div>
</template>

<script>
// import { handleError } from 'vue';
import BookGallery from "../book/BookGallery.vue";
export default {
  props: {
    Option: {
      type: Object,
      default: function () {
        return {
          category: "",
          vip: "",
          range: "",
          order: "",
          status: "",
          page: "",
        };
      },
    },
  },
  components: { BookGallery },
  name: "NovelList",
  data() {
    return {
      novelList: [
        {
          name: "武炼巅峰",
          author: "莫默",
          genre: "玄幻",
          status: "连载中",
          description: "一段传奇的修行历程。",
        },
        {
          name: "大道朝天",
          author: "血红",
          genre: "修真",
          status: "已完结",
          description: "充满哲理意味的仙侠之作。",
        },
        {
          name: "全职高手",
          author: "蝴蝶蓝",
          genre: "游戏",
          status: "已完结",
          description: "MMORPG游戏中的神话。",
        },
        // 其他书籍数据
      ],
      filteredNovelList: [],
      cod: "排序方法",
    };
  },
  computed: {
    // 添加 getter
    getFilteredNovelList() {
      if (this.$route.query.genre) {
        return this.novelList.filter((novel) => {
          return novel.genre === this.$route.query.genre;
        });
      } else {
        return this.novelList;
      }
    },
  },

  methods: {
    handleCommand(command) {
      // console.log(this.$refs);
      let books = this.$refs.child.books;
      console.log(books);

      if (command === "1") {
        books.sort((a, b) => b.rating - a.rating);
        this.cod = "按评分降序";
      }
      if (command === "2") {
        books.sort((a, b) => a.rating - b.rating);
        this.cod = "按评分升序";
      }
      if (command === "3") {
        books.sort((a, b) => b.cnt - a.cnt);
        this.cod = "按字数降序";
      }
      if (command === "4") {
        books.sort((a, b) => a.cnt - b.cnt);
        this.cod = "按字数升序";
      }
      if (command === "5") {
        books.sort((a, b) => b.fav - a.fav);
        this.cod = "按收藏降序";
      }
      if (command === "6") {
        books.sort((a, b) => a.fav - b.fav);
        this.cod = "按收藏升序";
      }
    },
    // f() {
    //   this.handleCommand("1");
    //   console.log("11");
    // },
    setFilteredNovelList(newValue) {
      this.filteredNovelList = newValue;
    },
  },
  // created(){
  //   this.f();
  // },

  watch: {
    "$route.query": function (newValue, oldValue) {
      if (newValue !== oldValue && newValue.genre) {
        this.setFilteredNovelList(
          this.novelList.filter((novel) => {
            return novel.genre === newValue.genre;
          })
        );
      } else {
        this.setFilteredNovelList(this.novelList);
      }
    },
  },
};
</script>

<style scoped>
.novel-item {
  margin-bottom: 20px;
}

.no-result {
  text-align: center;
  padding: 20px;
}
</style>
<style scoped>
.block-col-2 .demonstration {
  display: inline-block;
  /* 将 display 属性改为 inline-block */
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}

.rank-dropdown-menu {
  --el-dropdown-menuItem-hover-fill: #f56c6c;
  --el-dropdown-menuItem-hover-color: white;
}
</style>
