<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="setCatalogInvisiable"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel catalog">
      <h4 class="lang">目录</h4>
      <ul ref="clist" v-infinite-scroll="load">
        <li v-for="(chapter, chapterId) in chapters.slice(0, this.chapterVisiableCount)" :key="chapterId"
          :ref="'li' + chapterId"><a>{{
            chapter.name
          }}</a></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: "ReaderCatalogPanel",
  created() {
    this.chapterVisiableCount = parseInt(this.thisChapter / 20) * 20 + 60
  },
  mounted() {
    this.$refs["li" + this.thisChapter][0].classList.add('act')
  },
  data() {
    return {
      chapterVisiableCount: 20,
      thisChapter: 3,
      chapters: [
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
        { name: "陨落的天才" },
        { name: "斗气大陆" },
        { name: "客人" },
        { name: "云岚宗" },
        { name: "聚气散" },
        { name: "炼药师" },
        { name: "休！" },
        { name: "神秘的老者" },
        { name: "药老！" },
        { name: "借钱" },
        { name: "坊市" },
        { name: "离他远点" },
        { name: "黑铁片" },
        { name: "吸掌" },
      ],
    }
  },
  methods: {
    setCatalogInvisiable() {
      this.$parent.changeVisiable("catalog")
    },
    scrollToThisChapter() {
      this.$refs.clist.scrollTop = this.$refs["li" + this.thisChapter][0].offsetTop
    },
    load() {
      this.chapterVisiableCount += 20
    },
  },
}
</script>