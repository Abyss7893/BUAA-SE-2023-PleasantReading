<template>
  <div class="panel-box">
    <div class="panel comments">
      <h4 class="lang">评论</h4>
      <div class="comments-box">
        <ul v-infinite-scroll="load">
          <li v-for="(comment, commentId) in this.comments.slice(0, this.commentsNum)" :key="commentId">
            <div class="comment-avatar">
              <img :src="this.$store.state.userAvatar" alt="">
            </div>
            <div class="comment-text">
              <div class="comment-name">{{ this.$store.state.userInfo.username }}</div>
              <div class="comment-time">{{ parseTime(comment.timestamp) }}</div>
              <div class="comment-content" :ref="commentId" v-html="replaceLineBreaks(comment.text)"></div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: "MyComment",
  data() {
    return {
      commentsNum: 8,
      comments: []
    }
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments(){
      axios.get('http://154.8.183.51/book/comments')
      .then((data)=>{
        
        let len = data.data.comments.length
        for(var i=0;i<len;i++){
          this.comments.push(data.data.comments[i])
        }
      })
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
    load() {
      this.commentsNum += 8
    },
  },

}
</script>
<style scoped>
.lang {
  margin: 16px 0 12px 36px;
}
.comments {
  width: 677px;
  background-color: white;
  float: left;
  padding-bottom: 24px;
  padding-right: 24px;
}

.comments .comments-box {
  color: #262626;
}

.comments .comments-box ul {
  min-height: 315px;
  max-height: 450px;
  overflow: auto;
}
.comments .comments-box li {
  float: left;
  margin: 16px 0 0 32px;
  width: 600px;
  background-color: #94919120;
  border-radius: 12px;
  padding: 0 12px 12px 12px;
}



.comments .comments-box ul.no-comments {
  font: 16px/24px PingFangSC-Regular, -apple-system, Simsun;
  margin-top: 24px;
  height: 30px;
}

.comments .comments-box ul li.comment-list {
  margin-top: 16px;
  padding: 0 0 16px 10px;
  border-radius: 10px;
  min-height: 90px;
  float: left;
  position: relative;
  background-color: #94919120;
}

.comments .comments-box li .comment-avatar {
  margin-top: 16px;
  border-radius: 100%;
  background-color: rgba(255, 255, 255, 0);
  float: left;
  width: 48px;
  height: 48px;
  overflow: hidden;
}

.comments .comments-box li .comment-avatar img {
  width: 48px;
}

.comments .comments-box li .comment-text {
  float: left;
  width: 500px;
}

.comments .comments-box li .comment-name {
  /* float: left; */
  font: 10px/20px PingFangSC-Regular, -apple-system, Simsun;
  margin: 14px 0 0 10px;
  font-weight: 600;
}

.comments .comments-box li .comment-time {
  float: left;
  font: 12px/16px PingFangSC-Regular, -apple-system, Simsun;
  margin-left: 10px;
  /* padding-top: 19px; */
}

.comments .comments-box li .comment-content {
  float: left;
  font-family: STKaiti, Kaiti;
  margin: 2px 0 0 6px;
  width: 480px;
  /* height: 40px; */
  /* max-height: 40px; */
  word-wrap: break-word;
  transition: max-height 0.5s ease;
}

.comments .comments-box li i {
  position: absolute;
  top: 100%;
  left: 100%;
  margin-left: -30px;
  margin-top: -18px;
  cursor: pointer;
  color: #262626;
  transition: color .3s, background-color .3s;
  width: 20px;
  height: 12px;
  text-align: center;
  background-color: #94919120;
  border: 1px solid rgba(0, 0, 0, .1);
  border-radius: 4px;
}

.comments .comments-box li i:hover {
  color: #ed4259;
  border: 1px solid #ed425928;
  background-color: #ed425928;
}

.comments .comments-box li i:hover svg path {
  fill: #ed4259;
}

.comments .comments-box li i div {
  margin: -2px 0 0;
  font: 16px/20px PingFangSC-Regular, -apple-system, Simsun;
  line-height: 0;
}

.comment-input-box {
  border-top: 1px solid #e5e5e5;
  margin-top: 12px;
  padding-top: 12px;
}

.comment-input-box textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  font-family: STKaiti, Kaiti;
  outline: none;
  width: 100%;
  height: 45px;
  resize: none;
  white-space: pre-wrap;
  box-sizing: border-box;
  transition: height 0.3s ease;
}

.comment-input-box textarea:focus {
  height: 105px;
}

.comment-input-box input[type="button"] {
  float: right;
  margin-top: 12px;
  padding: 10px;
  width: 50px;
  background-color: #f56c6c;
  cursor: pointer;
  border: none;
  border-radius: 10px;
  color: #fff;
  font-size: 12px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  outline: none;
}

.comment-input-box input[type="button"]:hover {
  background-color: #d5190fde;
}
</style>