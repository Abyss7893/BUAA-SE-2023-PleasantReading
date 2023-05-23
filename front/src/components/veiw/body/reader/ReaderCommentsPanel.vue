<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="closeComments"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel comments">
      <h4 class="lang">评论</h4>
      <div class="comments-box">
        <ul v-infinite-scroll="load">
          <li v-for="(comment, commentId) in this.comments.slice(0, this.commentsNum)" :key="commentId">
            <div class="comment-avatar"></div>
            <div class="comment-text">
              <div class="comment-name">{{ comment.name }}</div>
              <div class="comment-time">{{ comment.time }}</div>
              <div class="comment-content" :ref="commentId" v-html="replaceLineBreaks(comment.content)"></div>
            </div>
            <i :style="{
              display: comment.content.length > 60 ? 'block' : 'none'
            }" @click="extendContent(commentId)">
              <div :ref="'i' + commentId"><svg class="icon" width="16" height="16" viewBox="0 0 1024 1024"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M182.857143 356.937143a27.062857 27.062857 0 0 1 36.571428 0l292.571429 292.571428 292.571429-292.571428a27.794286 27.794286 0 0 1 39.131428 39.131428l-310.857143 310.491429a26.697143 26.697143 0 0 1-36.571428 0L182.857143 395.337143a27.062857 27.062857 0 0 1 0-38.4z"
                    fill="#949191" />
                </svg></div>
            </i>
          </li>
        </ul>
        <div class="comment-input-box">
          <form action="POST"><textarea wrap="soft" rows="4" placeholder="发送一条友善的评论~"></textarea><input type="button"
              value="发送">
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "ReaderCommentsPanel",
  data() {
    return {
      commentsNum: 8,
      comments: [
        {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！\n原神真好玩！\n原神真好玩！\n原神真好玩！\n原神真好玩！\n原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        },
        {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！\n原神真好玩！\n原神真好玩！\n原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        }, {
          "name": "甘雨",
          "avatar": null,
          "time": "2023-01-25",
          "content": "原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！原神真好玩！",
        },
      ]
    }
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
    load() {
      this.commentsNum += 8
    },
  },

}
</script>
<style>
.reader-menu .comments .comments-box li .comment-content.extendHeight {
  height: auto;
}
</style>