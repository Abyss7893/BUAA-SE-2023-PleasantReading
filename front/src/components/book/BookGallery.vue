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
          <div class="book-item">
            <div class="book-img-box">
              <img :src="book.cover" alt="Book Cover" />
              <!-- <span>{{ book.cover }}</span> -->
            </div>
            <div class="book-mid-info">
              <h3 class="title">{{ book.title }}</h3>

              <div class="author">
                <p class="name">{{ book.author }}</p>

                <em>|</em>
                <p class="category">{{ book.category }}</p>
                <em>|</em>
                <span>连载</span>
              </div>

              <p class="intro">{{ book.summary }}</p>

              <div class="book-rating">{{ book.rating }}</div>

              <el-rate v-model="book.rating" :disabled="true"></el-rate>
              <p class="size">字数:114.5万字</p>
            </div>
          </div>
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
export default {
  components: {},
  data() {
    return {
      books: [
        {
          id: 1,
          title: "Book顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶 1",
          cover: require("assets/imgs/bookcv.png"),
          author: "Autdddddddddd顶顶顶顶顶顶顶顶顶顶ddddddddd",
          category: "Categd顶顶顶顶顶顶顶顶顶顶ory 1dddddddd",

          summary: "Sww",
          rating: 4.5,
        },
        {
          id: 2,
          title: "Book 2",
          cover: require("assets/imgs/bookcv.png"),
          author: "Authow",
          category: "Categorydddddddddddddssssssssssssssssss 2",
          summary: "Summary 2",
          rating: 1.2,
        },
        // Add more books as needed
      ],
      currentPage: 1, // 当前页数
      pageSize: 20,
    };
  },
  created() {
    this.generateTestData();
  },

  methods: {
    generateTestData() {
      //   const testData = [];
      for (let i = 3; i <= 205; i++) {
        this.books.push({
          id: i,
          title: `Book ${i}`,

          cover: require("assets/imgs/bookcv.png"),
          author: "Author",
          category: "Category",
          summary: "Summary",
          rating: 4.5,
        });
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
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
      console.log(tmpbook);
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
  },
};
</script>
  
<style scoped>
.book-gallery {
  /* display: flex; */
  border-left: 2px  solid #dfe1e3;
  padding-left:10px ;
  flex-wrap: wrap;
  justify-content: space-between;
}

.book-row {
  width: 100%;
  height: 220px;
  /* display: flex; */
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap; /* 添加该行 */
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

/* .book-cover{

} */
.book-cover img {
  /* position: absolute; */
  /* top: 100%;
  left: 50%; */
  /* display: block;
  min-width: 100%;
  min-height: 100%;
  transform: translate(-50%, -50%); */
}

.book-info {
  margin-left: 10px;
  text-overflow: ellipsis;
  text-align: left;
}

.book-rating {
  margin-top: auto;
  font-weight: bold;
}
</style>


<style scoped>
.book-img-box {
  display: block;

  height: 136px;
  margin-right: 16px;
  position: relative;
  /* max-width: 102px;
  min-width: 102px; */
  z-index: 3;
}
.book-mid-info {
  max-width: 280px;
  min-width: 280px;
  margin-top: 5px;
  float: left;
  overflow: hidden;
  text-overflow: ellipsis;
  /* white-space: nowrap; */

  /* text-overflow: ellipsis; */
}
.intro {
  color: #666;
  font-size: 14px;
  max-height: 48px;
  min-height: 48px;
  line-height: 24px;
  margin-bottom: 8px;
  overflow: hidden;
  text-overflow: ellipsis;

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
  /* text-overflow: ellipsis; */
  /* white-space: normal; */
  /* background: #030958; */
}
.author {
  height: 22px;
  margin-bottom: 6px;
  display: flex;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
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
</style>
