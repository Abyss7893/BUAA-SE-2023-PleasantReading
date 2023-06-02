<template>
  <div class="main-search-conten">
    <div v-if="bookids.length == 0">
      <div class="search-result-null" v-if="this.books.length == 0">
        <el-empty description="查询结果为空哦~" :image="require('assets/imgs/book_null.png')" image-size="300px" />
      </div>
    </div>
    <div v-if="bookids.length != 0">
      <div class="search-filter"></div>
      <div class="tool-bar"></div>
      <div class="result-list">
        <ul>
          <li v-for="(book, bookidx) in books" :key="bookidx">
            <BookInfoCompnent :book="book" />
          </li>
        </ul>
      </div>
      <div class="search-foot">
        <div class="page-control">

          <div class="arrow">
            <div class="left"><a @click="jumpToPage(this.$route.query.page - 1)"><el-icon>
                  <Back />
                </el-icon></a></div>
            <div class="page-num"><a v-text="this.$route.query.page + '/' + this.pages"></a></div>
            <div class="right"><a @click="jumpToPage(this.$route.query.page - (-1))"><el-icon>
                  <Right />
                </el-icon></a></div>
          </div>
          <div class="jump">
            <input ref="pageInput" type="text" :value="this.$route.query.page" class="page-input">
            <a class="go" @click="jumpToPage(this.$refs.pageInput.value)">跳转</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import 'css/search/search.css'
import { getBookDetiles, getSearchBookIds } from '@/api/api'
import BookInfoCompnent from './BookInfoCompnent.vue'
import { ElMessage } from 'element-plus'
export default {
  name: "seach-book",
  mounted() {
    this.getSearchBooks(this.$route.query.keywords, this.$route.query.page)
  },
  components: {
    BookInfoCompnent,
  },
  data() {
    return {
      bookids: [],
      pages: 0,
      books: [],
    }
  },
  methods: {
    getSearchBooks(keywords, page) {
      getSearchBookIds(keywords, page).then((data) => {
        if (data.status && data.status == 200) {
          this.bookids = data.data.books
          this.pages = data.data.pages
          if (this.$route.page > data.data.pages) {
            ElMessage({
              message: '非法页面访问！',
              grouping: true,
              type: 'error',
            })
           
            return
          }
          if (this.bookids.length == 0) {
            // alert("该查询结果为空！")
            return
          }
          for (let index = 0; index < this.bookids.length; index++) {
            getBookDetiles(this.bookids[index]).then((data) => {
              this.books.push(data)
            })
          }
        } else {
          ElMessage({
            message: '该关键词查询不到任何结果！',
            grouping: true,
            type: 'warning',
          })
          
        }
      })
    },
    jumpToPage(page) {
      if (isNaN(page)) {
        ElMessage({
          message: '非数字的页面请求',
          grouping: true,
          type: 'error',
        })
        
        return
      }
      if (page <= 0 || page > this.pages) {
        ElMessage({
          message: '请求页面超出范围哦',
          grouping: true,
          type: 'warning',
        })
        
        return
      }
      this.$router.push({ path: '/search', query: { "keywords": this.$route.query.keywords, "page": page } })
    },
  }
}
</script>
<style>
em {
  font-style: normal
}

.search-result-null {
  margin-top: 24px;
}
</style>