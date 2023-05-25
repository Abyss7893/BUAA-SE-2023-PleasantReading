<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="closeComments"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel comments">
      <h4 class="lang">评论</h4>
      <div class="comments-box">
        <ul v-infinite-scroll="load" v-if="this.comments.length > 0">
          <li v-for="(comment, commentId) in this.comments.slice(0, this.commentsNum)" :key="commentId">
            <div class="comment-avatar"><img :src="comment.img" alt=""></div>
            <div class="comment-text">
              <div class="comment-name">{{ comment.nickname }}</div>
              <div class="comment-time">{{ comment.timestamp }}</div>
              <div class="comment-content" :ref="commentId" v-html="replaceLineBreaks(comment.text)"></div>
            </div>
            <i v-show="isExtendDisplay(comment.text)" @click="extendContent(commentId)">
              <div :ref="'i' + commentId"><svg class="icon" width="16" height="16" viewBox="0 0 1024 1024"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M182.857143 356.937143a27.062857 27.062857 0 0 1 36.571428 0l292.571429 292.571428 292.571429-292.571428a27.794286 27.794286 0 0 1 39.131428 39.131428l-310.857143 310.491429a26.697143 26.697143 0 0 1-36.571428 0L182.857143 395.337143a27.062857 27.062857 0 0 1 0-38.4z"
                    fill="#949191" />
                </svg></div>
            </i>
          </li>
        </ul>
        <ul class="no-comments" v-if="this.comments.length == 0">还没有人留下评论，快来留下你的见解吧！</ul>
        <div class="comment-input-box">
          <form action="POST">
            <textarea ref="mycomment" wrap="soft" rows="1" placeholder="发送一条友善的评论~"></textarea><input type="button"
              value="发送" @click="submitComment">
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getBookComments, submitBookComment } from "@/api/api";
export default {
  name: "ReaderCommentsPanel",
  data() {
    return {
      commentsNum: 5,
      comments: []
    }
  },
  created() {
    this.$nextTick(this.initComments());
  },
  methods: {
    extendContent(commentId) {
      if (this.$refs[commentId][0].classList.contains("extendHeight")) {
        this.$refs[commentId][0].classList.remove("extendHeight")
        this.$refs['i' + commentId][0].innerHTML = ''
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 1024 1024');
        svg.setAttribute('width', '16');
        svg.setAttribute('height', '16');
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', 'M182.857143 356.937143a27.062857 27.062857 0 0 1 36.571428 0l292.571429 292.571428 292.571429-292.571428a27.794286 27.794286 0 0 1 39.131428 39.131428l-310.857143 310.491429a26.697143 26.697143 0 0 1-36.571428 0L182.857143 395.337143a27.062857 27.062857 0 0 1 0-38.4z');
        path.setAttribute('fill', '#949191');
        svg.appendChild(path);
        this.$refs['i' + commentId][0].appendChild(svg);
      }
      else {
        this.$refs[commentId][0].classList.add("extendHeight")
        this.$refs['i' + commentId][0].innerHTML = ""
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 1024 1024');
        svg.setAttribute('width', '16');
        svg.setAttribute('height', '16');

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', 'M533.333333 358.4l-332.8 332.8-29.866666-29.866667L533.333333 298.666667l362.666667 362.666666-29.866667 29.866667-332.8-332.8z');
        path.setAttribute('fill', '#949191');

        svg.appendChild(path);
        this.$refs['i' + commentId][0].appendChild(svg);
      }
    },
    closeComments() {
      this.$parent.changeComments()
    },
    replaceLineBreaks(text) {
      return text.replace(/\n/g, '<br>')
    },
    isExtendDisplay(text) {
      let line = 0
      let cnt = 0
      const pattern = /^[ -~]$/;
      for (let i = 0; i < text.length; i++) {
        const char = text.charAt(i)
        // 判断是否是换行符，并增加行数
        if (char === '\n') {
          line++
          cnt = 0
        } else {
          if (!pattern.test(char))
            cnt++
          else
            cnt += 0.5
          if (cnt == 30) {
            cnt = 0
            line++
          }
        }
      }
      if (cnt > 0)
        line++
      return line > 2
    },
    load() {
      if (this.commentsNum % 5 != 0)
        return
      this.commentsNum += 5
      this.getComments()
    },
    // 获取评论，一次五条
    getComments() {
      getBookComments(this.$route.params.bookid, this.$route.params.chapter, this.commentsNum / 5).then((data) => {
        let len = data.comments.length
        for (let index = 0; index < len; index++) {
          this.comments.push(data.comments[index])
        }
        this.commentsNum = this.comments.length
      });
    },
    submitComment() {
      if (this.$refs.mycomment.value.length === 0)
        return
      else if (this.$refs.mycomment.value.length > 500) {
        alert("评论不可以超过500字哦，请精简一下吧~")
        return
      }
      submitBookComment(this.$route.params.bookid, this.$route.params.chapter, this.$refs.mycomment.value).then((data) => {
        const code = data.request.status
        switch (code) {
          case 200:
            this.$refs.mycomment.value = ''
            location.reload();
            break;
          case 401:
            alert("用户未登录！或登录失效！请重新登录")
            this.$store.commit('refresh')
            break;
          default:
            break;
        }
      })
    },
    initComments() {
      this.getComments()
    },
  },

}
</script>
<style>
.reader-menu .comments .comments-box li .comment-content.extendHeight {
  max-height: 100px;
}
</style>