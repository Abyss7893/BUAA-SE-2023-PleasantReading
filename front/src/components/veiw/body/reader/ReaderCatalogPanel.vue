<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="setCatalogInvisiable"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel catalog">
      <h4 class="lang">目录</h4>
      <ul ref="clist">
        <li v-for="(chapter, chapterId) in chapters" :key="chapterId" :class="this.thisChapter == chapterId ? 'act' : ''"
          :ref="chapterId"><a :href="'/reader/' + this.$route.params.bookid + '/' + (chapterId + 1)">{{
            chapter
          }}</a></li>
      </ul>
    </div>
  </div>
</template>
<script>
import { getBookContent } from "@/api/api";

export default {
  name: "ReaderCatalogPanel",
  created() {
    this.thisChapter = parseInt(this.$route.params.chapter) - 1;
  },
  mounted() {
    this.initCatalog();
  },
  data() {
    return {
      chapterVisiableCount: 20,
      thisChapter: 1,
      chapters: [
        "目录加载中...",
      ],
    };
  },
  methods: {
    setCatalogInvisiable() {
      this.$parent.changeVisiable("catalog");
    },
    scrollToThisChapter() {
      this.$refs.clist.scrollTop = this.$refs[this.thisChapter][0].offsetTop
    },
    // load() {
    //   this.chapterVisiableCount += 20;
    //   if (this.chapters.length - this.chapterVisiableCount < 20)
    //     this.chapterVisiableCount = this.chapters.length
    // },
    initCatalog() {
      getBookContent(this.$route.params.bookid).then((data) => {
        this.chapters = data.outline;
        this.$nextTick(() => {
          this.chapterVisiableCount = parseInt(this.thisChapter / 20) * 20 + 60;
          // this.scrollToThisChapter()
        });
      });
    },
  },
}
</script>