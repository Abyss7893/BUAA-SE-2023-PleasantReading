<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center">
      <el-divider />
      <div v-if="mybooks.length === 0">
        <el-empty description="暂无书籍" :image="require('assets/imgs/book_null.png')" image-size="300px" />
      </div>
      <div v-else>
        <el-row v-for="ro in rownum - 1" :key="ro" gutter="60">
          <el-col v-for="o in colsize" :key="(ro - 1) * colsize + o - 1" :span="24 / colsize">
            <book-card :cover="mybooks[(ro - 1) * colsize + o - 1].cover" :name="mybooks[(ro - 1) * colsize + o - 1].name"
              :bookid="mybooks[(ro - 1) * colsize + o - 1].bookid"></book-card>
          </el-col>
          <el-divider />
        </el-row>
        <div v-if="mybooks.length - (rownum - 1) * colsize > 0">
          <el-row gutter="60">
            <el-col v-for="o in mybooks.length - (rownum - 1) * colsize" :key="(rownum - 1) * colsize + o - 1"
              :span="24 / colsize">
              <book-card :cover="mybooks[(rownum - 1) * colsize + o - 1].cover"
                :name="mybooks[(rownum - 1) * colsize + o - 1].name"
                :bookid="mybooks[(rownum - 1) * colsize + o - 1].bookid" />
            </el-col>
            <el-divider />
          </el-row>
        </div>
      </div>
    </div>
    <!-- </el-space> -->
  </head-and-foot>
</template>
    
<script>
import { getMyBook } from "@/api/api";
import HeadAndFoot from "../../HeadAndFoot.vue";
import BookCard from "./BookCard.vue";
// import CheckLogin from "../../../check/checkLogin.vue";
// import { nextTick } from "vue";

export default {
  components: { BookCard, HeadAndFoot, },
  data() {
    return {
      mybooks: [],
      rownum: 1,
      colsize: 6,
    };
  },
  methods: {},
  created() {
    // for (let i = 0; i < 99; i++) {
    //   this.mybooks.push({
    //     name: "逆天邪ddddddddddddddddddd神",
    //     cover: require("../../../../assets/imgs/bookcv.png"),
    //   });
    // }

    this.$nextTick(() => {
      getMyBook().then((data) => {
        // // console.log(data);
        try {
          if ("books" in data)
            for (let book of data.books) {
              this.mybooks.push({
                name: book.name,
                cover: book.cover,
                bookid: book.bookid,
              });
            }
          this.rownum = Math.ceil(this.mybooks.length / this.colsize);
        } catch (e) {
          console.log(e);
        }
        // // console.log(this.mybooks);
      });
    });
  },
};
</script>
    
<style lang="scss">
// 引入 css
@import url(../../../../assets/css/mybooks/mybook.css);
</style>
  