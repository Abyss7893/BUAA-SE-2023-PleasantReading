<template>
    <book-gallery/>
</template>

<script>
import BookGallery from '../../book/BookGallery.vue';
export default {
  components: { BookGallery },
  name: "NovelList",
  data() {
    return {
      novelList: [
        { name: "武炼巅峰", author: "莫默", genre: "玄幻", status: "连载中", description: "一段传奇的修行历程。" },
        { name: "大道朝天", author: "血红", genre: "修真", status: "已完结", description: "充满哲理意味的仙侠之作。" },
        { name: "全职高手", author: "蝴蝶蓝", genre: "游戏", status: "已完结", description: "MMORPG游戏中的神话。" },
        // 其他书籍数据
      ],
      filteredNovelList: []
    };
  },
  computed: {
    // 添加 getter
    getFilteredNovelList() {
      if (this.$route.query.genre) {
        return this.novelList.filter(novel => {
          return novel.genre === this.$route.query.genre;
        });
      } else {
        return this.novelList;
      }
    }
  },
  methods: {
    // 修改为普通方法
    setFilteredNovelList(newValue) {
      this.filteredNovelList = newValue;
    }
  },
  watch: {
    '$route.query': function (newValue, oldValue) {
      if (newValue !== oldValue && newValue.genre) {
        this.setFilteredNovelList(this.novelList.filter(novel => {
          return novel.genre === newValue.genre;
        }));
      } else {
        this.setFilteredNovelList(this.novelList);
      }
    }
  }
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
