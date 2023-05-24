<template>
  <head-and-foot>
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center">
      <el-divider />
      <el-row v-for="ro in rownum - 1" :key="ro" gutter="60">
        <el-col
          v-for="o in colsize"
          :key="(ro - 1) * colsize + o - 1"
          :span="24 / colsize"
        >
          <book-card
            :cover="mybooks[(ro - 1) * colsize + o - 1].cover"
            :name="mybooks[(ro - 1) * colsize + o - 1].name"
          ></book-card>
        </el-col>
        <el-divider />
      </el-row>
      <div v-if="mybooks.length % colsize > 0">
        <el-row gutter="60">
          <el-col
            v-for="o in mybooks.length % colsize"
            :key="(rownum - 1) * colsize + o - 1"
            :span="24 / colsize"
          >
            <book-card
              :cover="mybooks[(rownum - 1) * colsize + o - 1].cover"
              :name="mybooks[(rownum - 1) * colsize + o - 1].name"
            />
          </el-col>
          <el-divider />
        </el-row>
      </div>
    </div>
    <!-- </el-space> -->
  </head-and-foot>
</template>
    
  <script>
import { getMyBook } from "@/api/api";
import HeadAndFoot from "../../HeadAndFoot.vue";
import BookCard from "./BookCard.vue";

export default {
  components: { BookCard, HeadAndFoot },
  data() {
    return {
      mybooks: [],
      rownum: 0,
      colsize: 6,
    };
  },
  created() {
    // for (let i = 0; i < 99; i++) {
    //   this.mybooks.push({
    //     name: "逆天邪ddddddddddddddddddd神",
    //     cover: require("../../../../assets/imgs/bookcv.png"),
    //   });
    // }
    // this.rownum = Math.ceil(this.mybooks.length / this.colsize);
    getMyBook().then((data) => {
      for (let book of data["books"]) {
        this.mybooks.push(book);
      }
    });
  },
};
</script>
    
  <style lang="scss">
// 引入 css
@import url(../../../../assets/css/mybooks/mybook.css);
</style>
  