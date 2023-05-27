<template>
  <div class="book-rank">
    <h1 style="padding-bottom: 15px">小说排行榜！</h1>
    <!-- <transition name="el-zoom-in-top"> -->
    <!-- <el-divider width-="100%"></el-divider> -->
    <el-space direction="vertical" alignment="start" :size="30">
      <el-row style="width: 100%" gutter="30">
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="collectionlist" title="收藏总榜"></rank-card>
        </el-col>
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="ratelist" title="好评总榜"></rank-card>
        </el-col>
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="finished" title="完结总榜"></rank-card>
        </el-col>
      </el-row>
      <el-row style="width: 100%" gutter="30">
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="weekpoplist" title="人气周榜"></rank-card>
        </el-col>
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="monthpop" title="人气月榜"></rank-card>
        </el-col>
        <el-col span="8" style="max-width: 30%">
          <rank-card :booklist="yearpop" title="人气年榜"></rank-card>
        </el-col>
      </el-row>

    </el-space>
    <!-- </transition> -->
  </div>
</template>

<script>
import { getBookList } from "@/api/api";
import RankCard from "./RankCard.vue";
import { getBookDetiles } from "@/api/api";
export default {
  components: { RankCard },
  data() {
    return {
      booklist: [],
      collectionlist: [],
      ratelist: [],
      weekpoplist: [],
      monthpop: [],
      yearpop: [],
      finished: [],
    };
  },
  methods: {
    getSimpleSize(size) {
      if (size > 1000000) return "长篇";
      else if (size) return "中篇";
      return "短篇";
    },
    getCollectionList() {
      let optheon = {
        page: "1",
        order: "favorcnt",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.collectionlist[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
    getweekpoplist() {
      let optheon = {
        page: "1",
        order: "weekpop",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.weekpoplist[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
    getmonthpop() {
      let optheon = {
        page: "1",
        order: "monthpop",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.monthpop[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
    getyearpop() {
      let optheon = {
        page: "1",
        order: "yearpop",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.yearpop[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
    getfinished() {
      let optheon = {
        page: "1",
        order: "score",
        status: "完结",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.finished[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
    getRateList() {
      let optheon = {
        page: "1",
        order: "score",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            this.ratelist[i] = {
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            };
          });
        }
      });
      // let optheon2 = {
      //   page: "2",
      //   order: "favorcnt",
      // };
      // getBookList(optheon2).then((data) => {
      //   var list = data.books;
      //   for (let i = 0; i < list.length; i++) {
      //     getBookDetiles(list[i]).then((book) => {
      //       this.collectionlist[i+10] = {
      //         name: book.title,
      //         id: book.id,
      //         author: book.author,
      //         cover: book.cover,
      //         state: [
      //           book.vip ? "VIP" : "免费",
      //           book.category,
      //           this.getSimpleSize(book.cnt),
      //         ],
      //       };
      //     });
      //   }
      // });
    },
  },
  created() {
    for (let i = 0; i < 10; i++) {
      this.collectionlist.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
      this.ratelist.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
      this.weekpoplist.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
      this.monthpop.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
      this.yearpop.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
      this.finished.push({
        cover: require("../../../assets/imgs/img_loading.gif"),
        author: "加载中",
        name: "加载中",
        state: ["加载中", "加载中", "加载中"],
      });
    }

    this.getCollectionList();
    this.getRateList();
    this.getweekpoplist();
    this.getmonthpop();
    this.getyearpop();
    this.getfinished();
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