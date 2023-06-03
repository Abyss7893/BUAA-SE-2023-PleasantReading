<template>
  <div class="center-box">
    <a class="bookmark" @click="markTheChapter"><svg t="1684825313597" class="icon" viewBox="0 0 1024 1024" version="1.1"
        xmlns="http://www.w3.org/2000/svg" p-id="7433" width="48" height="48">
        <path
          d="M832 64v960L530.3 812.8c-11-7.7-25.7-7.7-36.7 0L192 1024V64c0-35.4 28.7-64 64-64h512c35.3 0 64 28.6 64 64z"
          p-id="7434" :fill="chapterInfo.marked ? '#FFD70077' : '#d8d8d8d1'"></path>
      </svg></a>
    <div class="text">
      <h1 class="chapter-title">
        {{ chapterInfo.chapterTitle }}
      </h1>
      <div class="info">
        <div class="book-name float"><svg t="1684560199171" class="icon" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="2519">
            <path
              d="M947.701961 623.435294l-694.713725 0q-11.043137 0-23.090196 6.023529t-22.588235 18.070588-17.066667 28.611765-6.52549 37.647059 5.521569 39.152941 14.556863 32.12549 22.086275 22.086275 28.109804 8.031373l693.709804 0q-12.047059-12.047059-21.082353-27.105882-8.031373-13.05098-14.556863-31.121569t-6.52549-41.160784q0-26.101961 6.52549-43.168627t14.556863-28.109804q9.035294-12.047059 21.082353-21.082353zM947.701961 897.505882q0 17.066667-22.086275 17.066667l-733.866667 0q-34.133333 0-57.223529-14.054902t-37.647059-38.65098-20.580392-58.729412-6.023529-73.286275l0-582.27451q0-77.301961 41.160784-111.937255t117.458824-34.635294l34.133333 0 68.266667 0 93.364706 0q51.2 0 104.909804-0.501961t104.909804-0.501961l94.368627 0 70.27451 0 35.137255 0q28.109804 0 49.192157 11.545098t35.137255 32.12549 21.584314 48.690196 7.529412 60.235294l0 406.588235q-191.74902 0-345.34902-1.003922l-128.501961 0q-64.25098 0-114.94902-0.501961t-83.827451-0.501961l-37.145098 0q-21.082353 0-41.160784 12.54902t-36.141176 34.133333-26.101961 50.196078-10.039216 59.733333q0 38.14902 10.541176 68.768627t27.607843 51.701961 37.647059 32.627451 40.658824 11.545098l685.678431 0q8.031373 0 14.556863 4.517647t6.52549 14.556863zM515.011765 0l0 388.517647 77.301961-108.423529 76.298039 108.423529 0-388.517647-153.6 0z"
              p-id="2520" fill="#f56c6c"></path>
          </svg>{{ bookInfo.bookName }}</div>
        <div class="book-author float"><svg t="1684561678490" class="icon" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="6600">
            <path
              d="M21.19936 958.08l-12.352-12.288a30.208 30.208 0 0 1-7.296-30.912l171.008-516.032c9.344-28.352 28.864-52.16 54.784-66.944L462.22336 211.2a30.208 30.208 0 0 1 36.352 4.864l308.032 308.096c9.6 9.6 11.648 24.448 4.928 36.288l-120.448 235.2c-14.72 25.856-38.528 45.44-66.816 54.848l-515.072 171.904a30.208 30.208 0 0 1-30.976-7.296l-13.312-13.312 304.832-304.896a60.16 60.16 0 0 0 58.88-15.104 61.12 61.12 0 0 0-0.96-86.464 61.12 61.12 0 0 0-86.464-1.024 60.16 60.16 0 0 0-15.168 58.88L21.19936 958.08zM745.74336 19.648l257.472 257.408c26.24 26.24 26.24 68.736 0 94.976L901.13536 474.112a30.208 30.208 0 0 1-42.752 0L548.75136 164.48a30.208 30.208 0 0 1 0-42.752L650.83136 19.648a67.2 67.2 0 0 1 94.912 0z"
              fill="#f56c6c" p-id="6601"></path>
          </svg>{{ bookInfo.bookAuthor }}</div>
        <div class="chapter-count float"><svg t="1684562374857" class="icon" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="30710">
            <path
              d="M640 85.3l200.8 200.8a42.7 42.7 0 0 1 12.5 30.2V896a42.7 42.7 0 0 1-42.7 42.7H213.3a42.7 42.7 0 0 1-42.7-42.7V128a42.7 42.7 0 0 1 42.7-42.7H640z m-85.3 256h-128v85.3h42.7v256h85.3V341.3z"
              p-id="30711" fill="#f56c6c"></path>
          </svg>{{ chapterInfo.chapterCount }}字</div>
      </div>
      <popOver>
        <div class="chapter-content">
          <p v-for="(paragraph, paragraphId) in chapterInfo.paragraphs" :key="paragraphId" :id="paragraphId">{{ paragraph
          }}</p>
        </div>
      </popOver>
    </div>
    <div class="chapter-control">
      <a @click="previousChapter">上一章</a>
      <span></span>
      <a :href="'/book/' + this.bookInfo.bookId">回到目录</a>
      <span></span>
      <a @click="nextChapter">下一章</a>
    </div>
  </div>
</template>
<script>
import 'css/reader/reader.css'
import { getBookDetiles, getBookCharpter, addBookmark, deletBookmark } from "@/api/api";
import { nextTick } from 'vue';
import { ElMessage } from 'element-plus';
import popOver from './popOver.vue';
import { mapGetters } from 'vuex';
export default {
  name: "ReaderComponent",
  data() {
    return {
      bookInfo: {
        bookId: 1,
        bookName: "加载中",
        bookAuthor: "加载中",
        chapterId: 1,
      },
      chapterInfo: {
        chapterTitle: "加载中",
        chapterCount: 9999,
        paragraphs: ["书籍内容正在赶来的路上，请耐心等待哟~"],
        marked: false,
      },
    }
  },
  components: {
    popOver,
  },
  computed: {
    ...mapGetters(['islogin'])
  },
  watch: {
    islogin() {
      this.initChapter()
    }
  },
  methods: {
    markTheChapter() {
      if (!this.chapterInfo.marked)
        addBookmark(this.$route.params.bookid, this.$route.params.chapter).then((data) => {
          const code = data.request.status
          switch (code) {
            case 200:
              ElMessage({
                message: '添加书签成功！',
                grouping: true,
                type: 'success',
              })
              this.chapterInfo.marked = true
              break
            case 401:
              ElMessage({
                message: '用户未登录！或登录失效！请重新登录',
                grouping: true,
                type: 'warning',
              })
              this.$store.commit('refresh')
              break;
            case 400:
              ElMessage({
                message: '书签已添加！',
                grouping: true,
                type: 'info',
              })
              break
            default:
              break;
          }
        })
      else
        deletBookmark(this.$route.params.bookid, this.$route.params.chapter).then((data) => {
          const code = data.request.status
          switch (code) {
            case 200:
              ElMessage({
                message: '删除书签成功！',
                grouping: true,
                type: 'success',
              })
              this.chapterInfo.marked = false
              break
            case 401:
              ElMessage({
                message: '用户未登录！或登录失效！请重新登录',
                grouping: true,
                type: 'warning',
              })
              this.$store.commit('refresh')
              break;
            case 400:
              ElMessage({
                message: '该处没有书签',
                grouping: true,
                type: 'info',
              })
              break
            default:
              break;
          }
        })
    },
    initChapter() {
      // console.log(0)
      // this.bookInfo.bookId =this.$route.params.bookid;
      this.bookInfo.chapterId = parseInt(this.$route.params.chapter);
      // console.log([this.bookInfo.bookId, this.bookInfo.chapterId]);
      getBookDetiles(this.$route.params.bookid).then((data) => {
        this.bookInfo.bookName = data.title;
        this.bookInfo.bookId = data.id;
        this.bookInfo.bookAuthor = data.author;
        // console.log(data);
        getBookCharpter(this.$route.params.bookid, this.$route.params.chapter).then((data) => {

          if (!data.status && data.response.status == 401) {
            this.$router.push('/book/' + this.$route.params.bookid)
            ElMessage({
              message: '该书籍仅供vip阅读！而您甚至未登录！',
              grouping: true,
              type: 'info',
            })
            return
          } else if (!data.status && data.response.status == 403) {
            this.$router.push('/book/' + this.$route.params.bookid)
            setTimeout(() => {
              ElMessage({
                message: '该书籍仅供vip阅读！',
                grouping: true,
                type: 'info',
              })
            }, 1000);

            return
          } else {
            let data2 = data.data
            this.chapterInfo.chapterTitle = data2.chaptertitle;//TODO
            this.chapterInfo.chapterCount = 0
            for (let index = 0; index < data2.content.length; index++) {
              this.chapterInfo.chapterCount += data2.content[index].length
            }
            this.chapterInfo.paragraphs = data2.content;
            this.chapterInfo.marked = data2.marked
          }
        });
      });
    },
    previousChapter() {
      if (this.bookInfo.chapterId == 1) {
        ElMessage({
          message: '本章为第一章，没有前一章节内容咯~',
          grouping: true,
          type: 'info',
        })
      } else {
        window.location.href = '/reader/' + this.$route.params.bookid + '/' + (this.$route.params.chapter - 1)
      }
    },
    nextChapter() {
      if (this.$parent.$refs.child1.$refs.child2.chapters.length == this.bookInfo.chapterId) {
        ElMessage({
          message: '本章为最后一章，没有后一章节内容咯~',
          grouping: true,
          type: 'info',
        })
      } else
        window.location.href = '/reader/' + this.$route.params.bookid + '/' + (parseInt(this.$route.params.chapter) + 1)
    },
  },
  created() {
    nextTick(this.initChapter());
    // this.initChapter()
  }
}
</script>