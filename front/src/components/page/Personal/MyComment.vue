<template>
    <div class="panel-box">
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
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "MyComment",
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
                }
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
.comments .comments-box li .comment-content.extendHeight {
    height: auto;
}
.panel-box .close-panel-button {
  cursor: pointer;
  position: absolute;
  left: 100%;
  margin-left: -36px;
  padding-top: 8px;
}

.panel-box .close-panel-button .close-panel-button-icon {
  transition: .5s;
}
.panel-box .close-panel-button .close-panel-button-icon:hover {
  color: #1a1a1a;
  transform: rotate(90deg);
}

.panel {
  border: 1px solid rgba(0, 0, 0, .1);
  padding: 40px 0 40px 24px;
  background-color: #fff;
  z-index: 100;
}

.panel h4 {
  font-size: 18px;
  line-height: 22px;
}

.setting li {
  margin-top: 30px;
}

.panel .setting-list li i {
  color: #666;
  display: inline-block;
  font: 12px/16px PingFangSC-Regular, -apple-system, Simsun;
  margin-right: 16px;
  min-width: 48px;
  vertical-align: middle;
}

.panel .button {
  padding: 36px 0 0;
  text-align: center;
}

.panel .button a {
  display: inline-block;
  letter-spacing: normal;
  vertical-align: middle;
  word-spacing: normal;
  border-radius: 2px;
  font: 14px/34px PingFangSC-Regular, -apple-system, Simsun;
  height: 34px;
  width: 100px;
}


.panel .button .save-button {
  background: #f56c6c;
  border-color: #f56c6c;
  color: #fff;
  position: relative;
  text-align: center;
  z-index: 1;
  transition: color .3s, background-color .3s;
}

.panel .button .cancel-button {
  height: 32px;
  line-height: 32px;
  margin-left: 40px;
  width: 98px;
  background: hsla(0, 0%, 100%, .5);
  border: 1px solid rgba(0, 0, 0, .2);
  position: relative;
  text-align: center;
  z-index: 1;
}

.panel .button .save-button:hover {
  background: #ed4259;
  border-color: #ed4259;
  color: #fff;
}


.comments {
  width: 650px;
  float: left;
  padding-bottom: 24px;
  padding-right: 24px;
}

.comments .comments-box {
  color: #262626;
}

.comments .comments-box ul {
  height: 300px;
  overflow: auto;
}

.comments .comments-box li {
  min-height: 100px;
  margin-top: 16px;
  float: left;
  position: relative;
}

.comments .comments-box li .comment-avatar {
  margin-top: 16px;
  border-radius: 100%;
  background-color: #1a1a1a;
  float: left;
  width: 48px;
  height: 48px;
}

.comments .comments-box li .comment-text {
  float: left;
  width: 500px;
}

.comments .comments-box li .comment-name {
  float: left;
  font: 16px/20px PingFangSC-Regular, -apple-system, Simsun;
  margin: 14px 0 0 10px;
}

.comments .comments-box li .comment-time {
  float: left;
  font: 12px/16px PingFangSC-Regular, -apple-system, Simsun;
  margin-left: 10px;
  padding-top: 19px;
}

.comments .comments-box li .comment-content {
  float: left;
  font-family: STKaiti, Kaiti;
  margin: 12px 0 0 10px;
  width: 500px;
  height: 40px;
  overflow: hidden;
}

.comments .comments-box li i {
  position: absolute;
  top: 100%;
  left: 100%;
  margin-left: -16px;
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




</style>