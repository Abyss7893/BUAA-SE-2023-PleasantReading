<template>
  <div class="main-search-conten">
    <div class="search-filter"></div>
    <div class="tool-bar"></div>
    <el-skeleton animated :loading="loading" :count="4">
      <template #template>
        <div class="result-list">
          <li>
            <el-skeleton-item variant="image" style="width: 120px; height: 160px; float: left;" />
            <div style="width: 100%;height: 24px;">
              <el-skeleton-item variant="h3" style="width: 64px; margin-left: 16px;float: left;" />
            </div>
            <div style="width: 600px;float: left;">
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;width: 160px;" />
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;float: left;width: 240px;" />
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;float: left;width: 360px;" />
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;float: left;width: 480px;" />
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;float: left;width: 600px;" />
              <el-skeleton-item variant="text" style="margin:8px 0 8px 16px;float: left;width: 720px;" />
            </div>
          </li>
        </div>
      </template>
      <div v-if="bookids.length == 0">
        <div class="search-result-null" v-if="this.books.length == 0">
          <el-empty description="查询结果为空哦~" :image="require('assets/imgs/book_null.png')" image-size="300px" />
        </div>
      </div>
      <div v-else>
        <div class="result-list">
          <ul>
            <li v-for="(book, bookidx) in books" :key="bookidx">
              <BookInfoCompnent :bookinfo="book" />
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
    </el-skeleton>
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
      loading: true,
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
            this.loading = false
            return
          }
          if (this.bookids.length == 0) {
            this.loading = false
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
        this.loading = false
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

.main-search-conten {
  min-height: 800px;
}
</style>