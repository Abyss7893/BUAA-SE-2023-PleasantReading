<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center">
      <el-divider />
      <!-- <little-card /> -->

      <el-row v-for="ro in rownum - 1" :key="ro" gutter="60">
        <el-col
          v-for="o in colsize"
          :key="(ro - 1) * colsize + o - 1"
          :span="24 / colsize"
        >
          <little-card />
        </el-col>
        <el-divider />
      </el-row>

      <div v-if="mybooks.length - (rownum - 1) * colsize > 0">
        <el-row gutter="60">
          <el-col
            v-for="o in mybooks.length - (rownum - 1) * colsize"
            :key="(rownum - 1) * colsize + o - 1"
            :span="24 / colsize"
          >
            <little-card />
          </el-col>
          <el-divider />
        </el-row>
      </div>
    </div>
    <!-- </el-space> -->
  </head-and-foot>
</template>
      
  <script>
// import { getMyBook } from "@/api/api";
import HeadAndFoot from "../../HeadAndFoot.vue";
import LittleCard from "../other/LittleCard.vue";
// import BookCard from "./BookCard.vue";
// import CheckLogin from "../../../check/checkLogin.vue";
// import { nextTick } from "vue";

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
    for (let i = 0; i < 99; i++) {
      this.mybooks.push({
        name: "逆天邪ddddddddddddddddddd神",
        cover: require("../../../../assets/imgs/bookcv.png"),
      });
    }
    this.rownum = Math.ceil(this.mybooks.length / this.colsize);
  },
};
</script>
      
  <style lang="scss">
// 引入 css
@import url(../../../../assets/css/mybooks/mybook.css);
</style>
    