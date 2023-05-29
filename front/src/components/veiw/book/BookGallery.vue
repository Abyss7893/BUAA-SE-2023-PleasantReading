<template>
  <div class="book-gallery">
    <!-- <div class="book-row" v-for="(row, rowIndex) in bookRows" :key="rowIndex"> -->
    <div
      class="book-row"
      v-for="(row, rowIndex) in displayedBooks"
      :key="rowIndex"
    >
      <!-- <el-col v-for="book in displayedBooks" :key="book.id" :span="12"> -->
      <el-row :gutter="40">
        <el-col v-for="book in row" :key="book.id" :span="12">
          <!-- </div> -->
          <book-mini-card :book="book"></book-mini-card>
        </el-col>
      </el-row>
      <el-divider />
    </div>
    <div class="pagination">
      <el-button
        type="danger"
        plain
        @click="firstPage"
        :disabled="currentPage === 1"
        >首页</el-button
      >
      <el-button
        type="danger"
        plain
        @click="previousPage"
        :disabled="currentPage === 1"
      >
        上一页
      </el-button>
      <!-- <div > -->
      <span class="nuber"> 第{{ this.currentPage }}页 </span>
      <!-- </div>/ -->
      <el-button
        type="danger"
        plain
        @click="nextPage"
        :disabled="currentPage * pageSize >= books.length"
      >
        下一页
      </el-button>
      <el-button
        type="danger"
        plain
        @click="lastPage"
        :disabled="currentPage * pageSize >= books.length"
      >
        尾页
      </el-button>
    </div>
  </div>
</template>
  
  
  
  
<script>
// import axios from 'axios';
import { getBookDetiles, getBookList } from "@/api/api";
import BookMiniCard from "./BookMiniCard.vue";
export default {
  components: { BookMiniCard },
  props: {
    Option: {
      type: Object,
      default: function () {
        return {
          category: "",
          vip: false,
          range: "",
          order: "",
          status: "",
          page: "",
        };
      },
    },
  },
  data() {
    return {
      books: [],
      currentPage: 1, // 当前页数
      pageSize: 10,
    };
  },
  created() {
    // this.generateTestData();
    var defaultOptions = this.Option;
    for (let key in defaultOptions) {
      // console.log(key, defaultOptions[key]);
      if (defaultOptions[key] === "null") defaultOptions[key] = "";
    }
    // console.log(defaultOptions);
    this.flashData(defaultOptions);
  },

  methods: {
    formatNumber(number) {
      if (number >= 100000) {
        const formattedNumber = (number / 10000).toFixed(1);
        return `${formattedNumber}万`;
      } else if (number >= 1000) {
        const formattedNumber = (number / 1000).toFixed(1);
        return `${formattedNumber}千`;
      } else {
        return number.toString();
      }
    },
    booksInit() {
      this.books = [];
      for (let i = 1; i <= 10; i++) {
        this.books.push({
          id: i,
          title: `Book ${i}`,
          status: "加载中",
          cover: require("assets/imgs/img_loading.gif"),
          author: "加载中",
          category: "加载中",
          summary: "加载中",
          vip: "加载中",
          rating: 0,
          size: 0,
          simpleSizes: "加载中",
        });
      }
    },

    generateTestData() {
      // const testData = [];
      for (let i = 3; i <= 205; i++) {
        this.books.push({
          id: i,
          title: `Book ${i}`,
          status: "连载",
          cover: require("assets/imgs/bookcv.png"),
          author: "Author",
          category: "Category",
          summary: "Summary",
          vip: "VIP",

          rating: (Math.random() * 4.5).toFixed(1),
          size: Math.round(Math.random() * 3000000),
          simpleSizes: this.getSimpleSize(Math.round(Math.random() * 3000000)),
        });
      }

      for (let book of this.books) {
        book.sizeString = this.formatNumber(book.size);
      }
    },
    flashData(defaultOptions) {
      this.booksInit();
      var booklist;
      getBookList(defaultOptions).then((res1) => {
        booklist = res1.books;
        let i = 0;
        if (booklist.length < 10)
          this.books = this.books.slice(0, booklist.length);
        let j = 0;
        for (let bookid of booklist) {
          getBookDetiles(bookid).then((res) => {
            var data = res;

            this.books[i] = {
              id: data.id,
              cover: data.cover,
              title: data.title,
              author: data.author,
              cnt: data.cnt,
              fav: data.favorcnt,
              size: this.formatNumber(data.cnt),
              category: data.category,
              rating: parseFloat(data.score).toFixed(1),
              summary: data.brief,
              vip: data.vip ? "VIP" : "免费",
              status: data.status,
              simpleSizes: this.getSimpleSize(data.cnt),
            };
            if (i === 1) {
              console.log(data);
              console.log(this.books[i]);
            }
            i++;
          });
          j++;
          if (j === 30) break;
        }
        const self = this;

        setTimeout(function () {
          while (j < booklist.length) {
            let bookid = booklist[j];

            getBookDetiles(bookid).then((res) => {
              var data = res;

              self.books[i] = {
                id: data.id,
                cover: data.cover,
                title: data.title,
                author: data.author,
                cnt: data.cnt,
                fav: data.favorcnt,
                size: self.formatNumber(data.cnt),
                category: data.category,
                rating: parseFloat(data.score).toFixed(1),
                summary: data.brief,
                vip: data.vip ? "VIP" : "免费",
                status: data.status,
                simpleSizes: self.getSimpleSize(data.cnt),
              };
              i++;
            });
            j++;
          }
        }, 1000);
      });
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
      // axios.post('/url')
    },
    firstPage() {
      this.currentPage = 1;
    },
    nextPage() {
      const totalPages = Math.ceil(this.books.length / this.pageSize);
      if (this.currentPage < totalPages) {
        this.currentPage++;
      }
    },
    lastPage() {
      this.currentPage = Math.ceil(this.books.length / this.pageSize);
    },
    getSimpleSize(size) {
      if (size > 1000000) return "长篇";
      else if (size) return "中篇";
      return "短篇";
    },
  },

  computed: {
    bookRows() {
      const rows = [];
      let row = [];
      for (let i = 0; i < this.books.length; i++) {
        row.push(this.books[i]);
        if (row.length === 2 || i === this.books.length - 1) {
          rows.push(row);
          row = [];
        }
      }
      return rows;
    },
    displayedBooks() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      const tmpbook = this.books.slice(startIndex, endIndex);
      // // console.log(tmpbook);
      const rows = [];
      let row = [];
      for (let i = 0; i < tmpbook.length; i++) {
        row.push(tmpbook[i]);
        if (row.length === 2 || i === tmpbook.length - 1) {
          rows.push(row);
          row = [];
        }
      }
      return rows;
    },
    // getSize(num){
    //   if(num>10000) return toString(num/10000) + "万"
    // }
  },
};
</script>
  
<style scoped>
.el-divider--vertical {
  /* display: inline-block; */
  width: 1px;
  height: 90%;
  /* margin: 0 8px; */
  vertical-align: middle;
  /* position: relative; */
}

.book-gallery {
  /* display: flex; */
  border-left: 2px solid #dfe1e3;
  padding-left: 10px;
  flex-wrap: wrap;
  justify-content: space-between;
}

.book-row {
  width: 100%;
  height: 220px;
  /* display: flex; */
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  /* 添加该行 */
}

.book-item {
  width: 100%;
  height: 100%;
  /* flex-basis: calc(50% - 10px);  */
  display: flex;

  margin: 0px;
  /* background: url("../../assets/imgs/shuqian.jpg") ; */
  background-size: 100% 100%;
  /* background-attachment: fixed; */
  /* background-color: aliceblue; */

  /* background-color: #3627076b; */
  padding: 10px;
  border-radius: 4px;
  text-align: left;
}

.book-info {
  margin-left: 10px;
  /* text-overflow: ellipsis; */
  text-align: left;
}

.book-rating-text {
  font-size: 12px;
  margin-top: auto;
  font-weight: bold;
}

.book-rating {
  display: flex;
}
</style>


<style scoped>
.book-img-box {
  display: block;

  height: 186px;
  max-height: 186px;
  margin-right: 16px;
  position: relative;
  /* max-width: 102px;
  min-width: 102px; */
  z-index: 3;
}

.book-img-box img {
  width: 100%;
  height: 100%;
  overflow: hidden;
  max-width: 136px;
  min-height: 186px;
  max-height: 186px;

  transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s;
  /* z-index: 10; */
}

.book-img-box img:hover {
  transform: scale(1.1);
}

.book-mid-info {
  max-width: 280px;
  min-width: 280px;
  margin-top: 5px;

  /* float: left;
  overflow: hidden;
  text-overflow: nowrap; */
  /* white-space: nowrap; */

  /* text-overflow: ellipsis; */
}

.intro {
  color: #743e13a6;
  font-size: 14px;
  max-height: 48px;
  min-height: 48px;
  line-height: 24px;
  margin-bottom: 8px;
  width: 100%;
  font-family: kaiti;

  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  /* 这里是超出几行省略 */
  overflow: hidden;

  /* overflow: hidden; */
}

.el-row {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
  max-height: 210px;
  min-height: 210px;
}

.el-col {
  max-height: 210px;
  min-height: 210px;
}

.title {
  color: #231e1e;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding: 0px;
  /* text-overflow: ellipsis; */
  /* white-space: normal; */
  /* background: #030958; */
}

.author {
  height: 22px;
  margin-bottom: 6px;
  display: flex;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  /* border-top:solid #c6b7b758; */
  /* overflow: hidden; */
}

.name {
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}

.category {
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}

.size {
  font-size: small;
  color: #666;
}

.pagination {
  /* 对其方式：右对齐 */
  float: right;
  height: 40px;
}

.nuber {
  min-width: 60px;
  max-width: 60px;
  width: 60px;
}

/* .book-rate {
  --el-rate-void-color: red;
} */
</style>

<!-- <style lang="scss" scoped>
// .use {
//   color: var(--el-rate-void-color);
// }
</style> -->

<!-- <style scoped>
.el-rate .el-rate__icon.is-active {
    color: rgba(255, 0, 0, 0.441) !important;
}
</style> -->