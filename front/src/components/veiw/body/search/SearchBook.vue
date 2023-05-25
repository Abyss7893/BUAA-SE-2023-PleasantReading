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
    }
  }
}
</script>
<style>
em {
  font-style: normal
}
</style>