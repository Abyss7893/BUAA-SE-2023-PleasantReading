<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center">
      <el-divider />
      <!-- <transition name="el-zoom-in-top"> -->
      <!-- <little-card /> -->
      <div v-if="mybooks.length > 0">
        <el-row v-for="ro in rownum - 1" :key="ro" gutter="60">
          <el-col v-for="o in colsize" :key="(ro - 1) * colsize + o - 1" :span="24 / colsize">
            <little-card :book="mybooks[(ro - 1) * colsize + o - 1]" />
          </el-col>
          <el-divider />
        </el-row>

        <div v-if="mybooks.length - (rownum - 1) * colsize > 0">
          <el-row gutter="60">
            <el-col v-for="o in mybooks.length - (rownum - 1) * colsize" :key="(rownum - 1) * colsize + o - 1"
              :span="24 / colsize">
              <little-card :book="mybooks[(rownum - 1) * colsize + o - 1]" />
            </el-col>
            <el-divider />
          </el-row>
        </div>
      </div>
      <!-- <transition name="el-fade-in"> -->
      <div v-if="mybooks.length === 0">
        <el-empty description="暂无书籍" :image="require('assets/imgs/book_null.png')" image-size="300px" />
      </div>
    </div>
    <!-- </el-space> -->
  </head-and-foot>
</template>
      
<script>
import { getMyBookMark } from "@/api/api";
import HeadAndFoot from "../../HeadAndFoot.vue";
import LittleCard from "../other/LittleCard.vue";

export default {
  components: { HeadAndFoot, LittleCard },
  data() {
    return {
      mybooks: [],
      rownum: 1,
      colsize: 6,
    };
  },
  methods: {},
  created() {
    this.$nextTick(() => {
      getMyBookMark().then((data) => {
        console.log(data.data);
        try {
          for (let book of data.data.markinfo) {
            this.mybooks.push(book);
          }
          this.rownum = Math.ceil(this.mybooks.length / this.colsize);
          console.log("mb", this.mybooks);
        } catch (e) {
          console.log(e);
        }
        //
      });
    });

  },
};
</script>
      
<style lang="scss">
// 引入 css
@import url(~assets/css/mybooks/mybook.css);
</style>
    