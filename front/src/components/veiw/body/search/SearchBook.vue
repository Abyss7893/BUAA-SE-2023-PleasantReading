<template>
  <div class="main-search-conten">
    <div class="search-filter"></div>
    <div class="tool-bar"></div>
    <div class="result-list">
      <ul>
        <li v-for="(book, bookidx) in books" :key="bookidx">
          <div class="book-info-cover"><a href=""><img :src="book.cover" alt=""></a></div>
          <div class="book-info-main">
            <h3><a :href="'/book' + '/' + book.id">{{ book.title }}</a></h3>
            <p class="info"><a :href="'/book' + '/' + book.id">{{ book.author }}</a><em>|</em><span>{{ book.category
            }}</span><em>|</em><span>{{
  book.status }}</span></p>
            <el-rate v-model="book.score" style="--el-rate-fill-color: #ff7d7dc9" :disabled="true"></el-rate>
            <p class="brief">{{ book.brief }}</p>
          </div>
          <div class="book-info-right">
            <p><span>{{ toHANZI(book.cnt) }}</span>总字数</p>
            <p><span>{{ toHANZI(book.favorcnt) }}</span>总收藏</p>
            <p class="button"><a :href="'/book' + '/' + book.id" class="book-details">书籍详情</a>
              <a class="add-favor" @click="addToFavor(book.id)">添加收藏</a>
            </p>
          </div>
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
</template>
<script>
import 'css/search/search.css'
import { addBookToFavor, getBookDetiles, getSearchBookIds } from '@/api/api'
export default {
  name: "seach-book",
  mounted() {
    this.getSearchBooks(this.$route.query.keywords, this.$route.query.page)
  },
  data() {
    return {
      bookids: [],
      pages: 0,
      books: [],
    }
  },
  methods: {
    toHANZI(number) {
      if (number > 10000)
        return (number * 1.0 / 10000).toFixed(2) + "万"
      return number
    },
    addToFavor(bookid) {
      addBookToFavor(bookid).then((data) => {
        const code = data.request.status
        switch (code) {
          case 200:
            alert("收藏成功！")
            break;
          case 401:
            alert("用户未登录！或登录失效！请重新登录")
            break;
          default:
            break;
        }
      })
    },
    getSearchBooks(keywords, page) {
      getSearchBookIds(keywords, page).then((data) => {
        if (data.status && data.status == 200) {
          this.bookids = data.data.books
          this.pages = data.data.pages
          if (this.$route.page > data.data.pages) {
            alert("非法页面访问！")
            return
          }
          if (this.bookids.length == 0) {
            alert("该查询结果为空！")
            return
          }
          for (let index = 0; index < this.bookids.length; index++) {
            getBookDetiles(this.bookids[index]).then((data) => {
              this.books.push(data)
            })
          }
        } else {
          alert("该关键词查询不到任何结果！")
        }
      })
    },
    jumpToPage(page) {
      if (isNaN(page)) {
        alert("非数字的页面请求!")
        return
      }
      if (page <= 0 || page > this.pages) {
        alert("请求页面超出范围哦!")
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
</style>