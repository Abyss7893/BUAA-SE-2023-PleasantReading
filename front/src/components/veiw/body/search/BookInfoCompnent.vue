<template>
  <div>
    <div class="book-info-cover"><a :href="'/book' + '/' + book.id"><img :src="book.cover" alt=""></a></div>
    <div class="book-info-main">
      <h3><a :href="'/book' + '/' + book.id">{{ book.title }}</a></h3>
      <p class="info"><a :href="'/author' + '/' + book.author">{{ book.author }}</a><em>|</em><span>{{
        book.category
      }}</span><em>|</em><span>{{
  book.status }}</span></p>
      <el-rate :value="book.score" style="--el-rate-fill-color: #ff7d7dc9" :disabled="true"></el-rate>
      <p class="brief">{{ book.brief }}</p>
    </div>
    <div class="book-info-right">
      <p><span>{{ toHANZI(book.cnt) }}</span>总字数</p>
      <p><span>{{ toHANZI(book.favorcnt) }}</span>总收藏</p>
      <p class="button"><a :href="'/book' + '/' + book.id" class="book-details">书籍详情</a>
        <a class="add-favor" @click="addToFavor(book.id)">添加收藏</a>
      </p>
    </div>
  </div>
</template>

<script>
import { addBookToFavor } from '@/api/api'
import { ElMessage } from 'element-plus';
import 'css/search/search.css'
export default {
  name: 'BookInfo',
  components: {},
  props: { book: Object, },
  data() {
    return {
    };
  },
  watch: {},
  computed: {},
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
            ElMessage({
              message: '收藏成功',
              grouping: true,
              type: 'success',
            })
            
            break;
          case 401:
            ElMessage({
              message: '用户未登录！或登录失效！请重新登录',
              grouping: true,
              type: 'warning',
            })
            
            this.$store.commit('refresh')
            break;
          default:
            break;
        }
      })
    },
  },
  created() { },
  mounted() { }
};
</script>
<style lang="scss" scoped></style>