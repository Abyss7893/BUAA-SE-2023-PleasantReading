<template>
  <div class="book-rank">
    <h1 style="padding-bottom: 15px">小说排行榜！</h1>
    <!-- <transition name="el-zoom-in-top"> -->
      <!-- <el-divider width-="100%"></el-divider> -->
      <el-space direction="vertical" alignment="start" :size="30">
        <el-row style="width: 100%" gutter="20">
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="收藏周榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="人气周榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="好评周榜"></rank-card>
          </el-col>
        </el-row>
        <el-row style="width: 100%" gutter="20">
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="收藏月榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="人气月榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="好评月榜"></rank-card>
          </el-col>
        </el-row>
        <el-row style="width: 100%" gutter="20">
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="收藏总榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="人气总榜"></rank-card>
          </el-col>
          <el-col span="8" style="max-width: 30%">
            <rank-card :booklist="booklist" title="好评总榜"></rank-card>
          </el-col>
        </el-row>
      </el-space>
    <!-- </transition> -->
  </div>
</template>

<script>
import RankCard from "./RankCard.vue";
export default {
  components: { RankCard },
  data() {
    return {
      booklist: [],
    };
  },
  created() {
    for (let i = 0; i < 10; i++) {
      this.booklist.push({
        cover: require("../../../assets/imgs/bookcv.png"),
        author: "唐氏三少",
        name: "斗罗大陆",
        state: ["VIP", "玄幻", "短篇"],
      });
    }
  },
};
</script>

<style>
.book-rank {
  /* display: flex; */
  border-left: 2px solid #dfe1e3;
  padding-left: 10px;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>