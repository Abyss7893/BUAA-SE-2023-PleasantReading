<template>
  <div class="panel-box">
    <!-- <div class="mask" v-if="showMyCard"></div> -->
    <!-- <MyCard class="mycard" v-if="showMyCard" @close="showMyCard = false" :userID="currentId"></MyCard> -->
    <el-dialog v-model="showMyCard" :destroy-on-close="true" width="500px">
      <PersonalInfo :userID="currentId" :userImg="currentImg"></PersonalInfo>
    </el-dialog>
    <a class="close-panel-button" @click="closeComments"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel comments">
      <h4 class="lang">评论</h4>
      <div class="comments-box">
        <ul v-if="this.comments.length > 0">
          <li class="comment-list" v-for="(comment, commentId) in this.comments.slice(0, this.commentsNum)"
            :key="commentId">
            <div class="comment-avatar"><img :src="comment.img" alt=""
                @click="showPersonInfo(comment.userID, comment.img)"></div>
            <div class="comment-text">
              <div class="comment-name">{{ comment.nickname }}</div>
              <div class="comment-time">{{ parseTime(comment.timestamp) }}</div>
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
        <el-pagination small hide-on-single-page layout="prev, pager, next" :total="pages * 5" :page-size="5"
          @current-change="handleCurrentChange" :current-page="thisPage" class="page-control"></el-pagination>
        <div class="no-comments" v-if="this.comments.length == 0"><el-empty description="还没有人留下评论，快来留下你的足迹吧！"
            :image="require('assets/imgs/comment_null.png')" image-size="250px" /></div>
        <div class="comment-input-box">
          <textarea v-model="mycomment" wrap="soft" rows="1" placeholder="发送一条友善的评论~"></textarea><input type="button"
            value="发送" @click="submitComment">
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getBookComments, submitBookComment } from "@/api/api";
import { encodeForHTML } from "@/XSS/encode"
import PersonalInfo from "@/components/page/Personal/PersonalInfo.vue";
import { ElMessage } from "element-plus";
export default {
  name: "ReaderCommentsPanel",
  components: { PersonalInfo },
  data() {
    return {
      currentId: null,
      currentImg: "",
      showMyCard: false,
      pages: 1,
      thisPage: 1,
      mycomment: "",
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
    showPersonInfo(userid, userimg) {
      this.showMyCard = true;
      this.currentId = userid;
      this.currentImg = userimg
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
    parseTime(time) {
      var date = new Date(time);
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var hour = date.getHours();
      var minute = date.getMinutes();
      return year + "年" + month + "月" + day + "日" + hour + "时" + minute + "分"
    },
    // 获取评论，一次五条
    getComments() {
      getBookComments(this.$route.params.bookid, this.$route.params.chapter, 1).then((data) => {
        let len = data.comments.length
        for (let index = 0; index < len; index++) {
          for (let key in data.comments[index]) {
            if (key != "img")
              data.comments[index][key] = encodeForHTML(data.comments[index][key])
          }
          this.comments.push(data.comments[index])
        }
        this.pages = parseInt(data.pages)
      });
    },
    handleCurrentChange(val) {
      this.thisPage = val
      getBookComments(this.$route.params.bookid, this.$route.params.chapter, val).then((data) => {
        this.comments = []
        let len = data.comments.length
        for (let index = 0; index < len; index++) {
          for (let key in data.comments[index]) {
            if (key != "img")
              data.comments[index][key] = encodeForHTML(data.comments[index][key])
          }
          this.comments.push(data.comments[index])
        }
        this.pages = parseInt(data.pages)
      })
    },
    submitComment() {
      if (this.mycomment.length === 0)
        return
      else if (this.mycomment.length > 500) {
        ElMessage({
          message: '评论不可以超过500字哦，请精简一下吧~',
          grouping: true,
          type: 'info',
        })

        return
      }
      submitBookComment(this.$route.params.bookid, this.$route.params.chapter, this.mycomment).then((data) => {
        const code = data.request.status
        switch (code) {
          case 200:
            this.mycomment = ''
            this.handleCurrentChange(1)
            break;
          case 401:
            ElMessage({
              message: '用户未登录！或登录失效！请重新登录',
              grouping: true,
              type: 'waring',
            })

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

.mask {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 111;
  width: 100%;
  height: 100%;
  background-color: rgba(254, 253, 253, 0.5);
}

.mycard {
  z-index: 1000;
}

.page-control {
  height: 24px;
  margin: 16px 0 10px;
  float: right;
  --el-pagination-hover-color: #f03636;
  --el-pagination-bg-color: rgba(249, 240, 223, 0.543);
  --el-pagination-button-disabled-bg-color: rgba(250, 245, 235, 0.8);
}

.panel-box .el-dialog {
  margin: auto;
  width: 440px;
  background: linear-gradient(45deg, #fbda61, #ff5acd);
}

.panel-box .el-dialog__headerbtn svg path {
  fill: #fbda61;
}

.panel-box .el-dialog__headerbtn:hover svg path {
  fill: #fb526bf2;
}

.panel-box .el-overlay-dialog {
  display: flex;
  justify-content: center;
  vertical-align: center;
}

.panel-box .el-dialog__body {
  font-size: 18px;
  display: flex;
  justify-content: center;
}
</style>