<template>
  <head-and-foot>
    <div class="detail box-center">
      <div class="detail-content">
        <div class="detail-content-top">
          <div class="book-infos-view">
            <div class="book-infos">
              <div class="book-img-box-detail">
                <img :src="detailData.cover" />
              </div>
              <div class="book-info-box">
                <h1 class="book-name flex-view">
                  {{ detailData.title }}
                  <span>
                    <a :href="'/author/' + detailData.author" class="author-name">{{ detailData.author }}著</a>
                  </span>
                </h1>
                <!-- <el-divider></el-divider> -->

                <div class="book-state">
                  <span class="state hidden-sm">{{ detailData.status }}</span>
                  <span class="state hidden-sm">{{ detailData.vip }}</span>
                  <span class="state hidden-sm">{{
                    detailData.simpleSizes
                  }}</span>
                  <span class="state hidden-sm">{{ detailData.category }}</span>
                </div>
                <div class="translators flex-view" style="">
                  <span>字数：</span>
                  <span class="name">{{ detailData.size }}</span>
                </div>
                <div class="translators flex-view" style="">
                  <span class="rate-text">评分：</span>
                  <span class="name rate-text">{{ detailData.rating }}</span>
                  <el-rate v-model="detailData.rating" style="--el-rate-fill-color: #ff7d7dc9" :disabled="true"></el-rate>
                  <!-- <span class="name">{{ detailData.size }}</span> -->
                </div>

                <!-- <div class="translators flex-view" style="">
                  <span>分类：</span>
                  <span class="name">{{ detailData.category }}</span>
                </div> -->
                <div class="translators flex-view" style="">
                  <span>简介：</span>
                  <span class="name">{{ detailData.intro }}</span>
                </div>
              </div>
            </div>

            <div class="book-counts hidden-sm">
              <div class="count-item flex-view pointer" @click="gotoRead()">
                <div class="count-box flex-view">
                  <div class="count-text-box">
                    <span class="count-title">开始阅读</span>
                  </div>
                  <div class="count-num-box">
                    <span class="num-text">{{ detailData.wish_count }}</span>
                  </div>
                </div>
              </div>
              <div v-if="!isColected" class="count-item flex-view pointer" @click="collect()">
                <div class="count-box flex-view">
                  <div class="count-text-box">
                    <span class="count-title">收藏</span>
                  </div>
                </div>
              </div>
              <div v-if="isColected" class="count-item flex-view pointer" @click="collect()">
                <div class="count-box flex-view">
                  <div class="count-text-box">
                    <span class="count-title">已收藏</span>
                  </div>
                </div>
              </div>
              <!-- <div class="count-item flex-view pointer" @click="comment()">
                <div class="count-box flex-view">
                  <div class="count-text-box">
                    <span class="count-title">评论</span>
                  </div>
                </div>
              </div> -->
              <div class="count-item flex-view pointer" @click="showRate = !showRate">
                <div class="count-box flex-view">
                  <div class="count-text-box">
                    <span class="count-title">评分</span>
                  </div>
                </div>
              </div>
              <div v-if="showRate" class="translators flex-view" style="flex-direction: column">
                <!-- <span class="rate-text">评分：</span> -->
                <!-- <span class="name rate-text">{{ detailData.rating }}</span> -->
                <div class="rate-loyar">
                  <el-rate v-model="valueRate" allow-half style="--el-rate-fill-color: #ff7d7dc9"
                    :texts="['shit', '厕纸', '一般', '好好好', '神中神']" show-text></el-rate>
                </div>
                <div>
                  <el-button type="danger" plain size="small" @click="submitRate">提交</el-button>
                </div>
                <!-- <span class="name">{{ detailData.size }}</span> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <transition name="el-zoom-in-top">
        <div v-show="isContent">
          <el-divider>
            目录
            <el-icon v-show="Order" @click="changeOrder" style="--color: #315c9e">
              <SortDown />
            </el-icon>
            <el-icon v-show="!Order" @click="changeOrder" style="--color: #315c9e">
              <SortUp />
            </el-icon>
          </el-divider>

          <div class="novel-directory">
            <div v-for="(row, index) in rows" :key="index" class="directory-row">
              <!-- <a href="#"> -->
              <div v-for="chapter in row" :key="chapter.id" class="chapter-title" @click="gotoReadChapter(chapter.id)">
                {{ chapter.title }}
              </div>
              <!-- </a> -->
            </div>
          </div>

          <div class="book-content-view flex-view">
            <div class="main-content"></div>
          </div>
        </div>
      </transition>
      <div v-show="!isContent"></div>
    </div>
  </head-and-foot>
</template>


<script>
import { ref } from "vue";
import { submitRating } from "@/api/api";
import {
  getBookDetiles,
  getBookContent,
  addColection,
  deleteColection,
  getMyRating,
} from "@/api/api";
import HeadAndFoot from "../HeadAndFoot.vue";
import { ElMessage } from "element-plus";
// import getBookContent from
export default {
  components: { HeadAndFoot },
  data() {
    return {
      valueRate: ref(),
      isColected: false,
      showRate: false,
      Order: true,
      bookId: "",
      detailData: {
        cover: require("assets/imgs/img_loading.gif"),
        title: "正在加载",
        author: "正在加载",
        size: "0",
        category: "正在加载",
        rating: 0,
        intro: "正在加载",
        vip: "正在加载",
        status: "正在加载",
        simpleSizes: "正在加载",
      },
      tabUnderLeft: 6,
      tabData: ["简介", "评论"],
      selectTabIndex: 0,
      commentData: [],
      recommendData: [],
      sortIndex: 0,
      order: "recent", // 默认排序最新
      chapters: [
        // 添加更多章节数据
      ],
      isContent: true,
    };
  },
  computed: {
    rows() {
      const rowCount = Math.ceil(this.chapters.length / 3);
      const rows = [];

      for (let i = 0; i < rowCount; i++) {
        const startIndex = i * 3;
        const endIndex = startIndex + 3;
        const row = this.chapters.slice(startIndex, endIndex);
        rows.push(row);
      }

      return rows;
    },
  },
  methods: {
    collect() {
      if (!this.$store.state.isLogin) {
        ElMessage.warning("用户未登录，请先登录在收藏哦QAQ~")
        return;
      }
      var bookid = this.bookId;
      if (!this.isColected)
        addColection(bookid).then((bool) => {
          console.log(bool);
          if (bool) {
            this.isColected = true;
          }
        });
      else {
        deleteColection(bookid).then((bool) => {
          console.log(bool);
          if (bool) {
            this.isColected = false;
          }
        });
      }
    },
    submitRate() {
      submitRating(this.bookId, this.valueRate).then((date) => {
        if (date) {
          this.alertMessage();
        }
      });
    },
    alertMessage() {
      ElMessage({
        message: `评分成功！分数:${this.valueRate}`,
        type: "success",
      });
    },
    generateChater() {
      // for (let i = 1; i <= 400; i++) {
      //   i;
      //   this.chapters.push({ id: i, title: "Chapter " + i });
      // }
      getBookContent(this.bookId).then((bookContents) => {
        // console.log(bookContents);
        for (let content of bookContents.outline) {
          this.chapters.push(content);
        }
      });
    },
    changeOrder() {
      this.Order = !this.Order;
      this.chapters.reverse();
    },
    comment() {
      this.isContent = !this.isContent;
    },
    initRating() {
      getMyRating(this.bookId).then((response) => {
        if (response.status == 200) {
          if (response.data.message === "success")
            this.valueRate = parseFloat(response.data.score);
        } else { console.log("没有提交过评分") }

      }



      );
    },
    formatNumber(number) {
      if (number >= 100000) {
        const formattedNumber = (number / 10000).toFixed(1);
        return `${formattedNumber}万`;
      } else if (number >= 1000) {
        const formattedNumber = (number / 1000).toFixed(1);
        return `${formattedNumber}千`;
      } else {
        return number.toString();
      }
    },
    gotoRead() {
      this.$router.push({
        path: "/reader/" + this.bookId + "/1",
      });
    },
    gotoReadChapter(chapterId) {
      this.$router.push({
        path: "/reader/" + this.bookId + "/" + chapterId,
      });
    },
  },
  created() {
    this.bookId = this.$route.params.id;
    this.initRating();
    getBookDetiles(this.bookId).then((data) => {
      // console.log(data);
      this.isColected = data.fav;
      // console.log(data);
      this.detailData = {
        cover: data.cover,
        title: data.title,
        author: data.author,
        size: this.formatNumber(data.cnt),
        category: data.category,
        rating: parseFloat(data.score).toFixed(1),
        intro: data.brief,
        vip: data.vip ? "VIP" : "免费",
        status: data.status,
      };
      if (data.cnt > 1000000) this.detailData.simpleSizes = "长篇";
      else if (data.cnt > 200000) this.detailData.simpleSizes = "中篇";
      else this.detailData.simpleSizes = "短篇";
    });
    // this.generateChater();
    getBookContent(this.bookId).then((bookContents) => {
      console.log(bookContents);
      let i = 1;
      for (let content of bookContents.outline) {
        this.chapters.push({ id: i, title: content });
        i++;
      }
    });
    // 根据图书ID进行进一步的数据加载或处理
  },
};
</script >
<style scoped lang="less">
.rate-text {
  padding-top: 6px;
  padding-right: 4px;
}

.author-name {
  padding-left: 30px;
  font-size: 12px;
  font-family: kaiti;
}

.author-name:hover {
  color: #f56c6c;
}

.box-center {
  margin-left: auto;
  margin-right: auto;
  width: 1200px;
  border-left: solid 1px rgba(255, 0, 0, 0.13);
  border-right: solid 1px rgba(255, 0, 0, 0.13);
  // background-color: rgba(99, 93, 93, 0.039);
  border-radius: 1%;
  box-shadow: inset 0 1px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.el-divider--horizontal {
  display: block;
  height: 1px;
  width: 100%;
  margin: 7px 0;
  border-top: 1px var(--el-border-color) var(--el-border-style);
}

.hide {
  display: none;
}

.detail-content {
  display: flex;
  flex-direction: column;
  width: 1100px;
  margin: 4px auto;
}

.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.hidden-lg {
  display: none !important;
}

.book-infos-view {
  display: flex;
  margin: 89px 0 40px;
  overflow: hidden;

  .book-infos {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    display: flex;
    // margin: 6px 0;
  }

  .mobile-share-box {
    height: 38px;
    background: transparent;
    padding: 0 16px;
    margin: 12px 0;
    font-size: 0;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;

    .state {
      width: 64px;
      height: 24px;
      line-height: 24px;
      background: rgba(70, 132, 226, 0.1);
      border-radius: 2px;
      font-weight: 500;
      font-size: 12px;
      color: #4684e2;
      text-align: center;
    }

    .share-img {
      background: #fff;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      text-align: center;

      img {
        position: relative;
        top: 4px;
        width: 24px;
      }
    }
  }

  .book-img-box-detail {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 235px;
    flex: 0 0 235px;
    margin: 15px 0 15px 0;

    img {
      width: 158px;
      height: 211px;
      display: block;
      margin: 0 auto;
      border: 1px solid #eee;
      border-radius: 4px;
      box-shadow: 0 4px 8px 0 rgba(90, 8, 8, 0.322),
        0 6px 20px 0 rgba(49, 0, 0, 0);
      transition: 0.5s;
    }

    img:hover {
      scale: 1.1;
    }
  }

  .book-info-box {
    text-align: left;
    padding: 0;
    margin: 0;
  }

  .book-state {
    padding-top: 10px;
    height: 26px;
    line-height: 26px;

    .state {
      font-weight: 500;
      color: #4684e2;
      background: rgba(70, 132, 226, 0.1);
      border-radius: 2px;
      padding: 5px 8px;
      margin-right: 16px;
    }

    span {
      font-size: 14px;
      color: #152844;
    }
  }

  .book-name {
    font-size: 24px;
    line-height: 32px;
    margin: 0 0;
    vertical-align: bottom;
    border-bottom: solid #6666663c;
  }

  .translators,
  .authors {
    line-height: 18px;
    font-size: 14px;
    margin: 6px 0;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start;

    .name {
      max-width: 500px;
      color: #315c9e;
      white-space: normal;
      max-height: 200px;
      word-break: break-all;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 4;
      /* 这里是超出几行省略 */
      overflow: hidden;
    }
  }

  .tags {
    position: absolute;
    bottom: 20px;
    margin-top: 16px;

    .category-box {
      color: #152844;
      font-size: 14px;

      .title {
        color: #787878;
      }
    }
  }

  .book-counts {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 235px;
    flex: 0 0 235px;
    margin-left: 20px;
  }

  .pointer {
    cursor: pointer;
  }

  .count-item {
    height: 64px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    cursor: pointer;
  }

  .count-img {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 32px;
    flex: 0 0 32px;
    margin-right: 24px;
    font-size: 0;

    img {
      width: 100%;
      display: block;
    }
  }

  .count-box {
    position: relative;
    border-bottom: 1px solid #cedce4;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;

    height: 100%;
  }

  .count-box:hover {
    border-bottom: 3px solid #f73f1152;
  }

  .count-text-box {
    font-size: 0;

    .count-title {
      color: #152844;
      font-weight: 600;
      font-size: 16px;
      line-height: 18px;
      display: block;
      height: 18px;
    }

    // .count-title:hoe {
    //   color: #152844;
    // }
  }

  .count-num-box {
    font-weight: 600;
    font-size: 20px;
    line-height: 24px;
    color: #152844;
  }
}

.buy-way {
  overflow: hidden;

  .title {
    font-weight: 600;
    font-size: 18px;
    height: 26px;
    line-height: 26px;
    color: #152844;
    margin-bottom: 12px;
  }

  .buy-way-item {
    background: #fbfeff;
    border: 1px solid #cedce4;
    border-radius: 4px;
    -webkit-box-flex: 0;
    margin-right: 20px;
    -ms-flex: 0 0 255px;
    flex: 0 0 255px;
    padding: 10px;

    .name {
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      color: #152844;
      height: 24px;
      margin-bottom: 12px;
    }

    .price {
      position: relative;
      line-height: 24px;
    }

    .price-text {
      color: #ff7b31;
      font-size: 18px;
      font-weight: 700;
    }

    .buy-btn {
      cursor: pointer;
      display: block;
      background: #4684e2;
      border-radius: 4px;
      text-align: center;
      color: #fff;
      font-size: 14px;
      height: 32px;
      line-height: 32px;
      width: 76px;
      outline: none;
      border: none;
      margin-top: 12px;
    }

    .buy-btn img {
      width: 12px;
      margin-right: 2px;
      vertical-align: middle;
    }

    .buy-btn span {
      vertical-align: middle;
    }
  }
}

.book-content-view {
  margin-top: 40px;
  padding-bottom: 50px;
}

.main-content {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;

  .text {
    color: #484848;
    font-size: 16px;
    line-height: 26px;
    padding-left: 12px;
    margin: 11px 0;
    white-space: pre-wrap;
  }
}

.main-tab {
  border-bottom: 1px solid #cedce4;
}

.order-view {
  position: relative;
  color: #6c6c6c;
  font-size: 14px;
  line-height: 40px;

  .title {
    margin-right: 8px;
  }

  .tab {
    margin-right: 20px;
    cursor: pointer;
    color: #5f77a6;
    font-size: 16px;
    cursor: pointer;
  }

  .tab-select {
    color: #152844;
    font-weight: 600;
  }

  .tab-underline {
    position: absolute;
    bottom: 0;
    left: 84px;
    width: 16px;
    height: 4px;
    background: #4684e2;
    -webkit-transition: left 0.3s;
    transition: left 0.3s;
  }
}

.recommend {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 235px;
  flex: 0 0 235px;
  margin-left: 20px;

  .title {
    font-weight: 600;
    font-size: 18px;
    line-height: 26px;
    color: #152844;
    margin-bottom: 12px;
  }

  .books {
    border-top: 1px solid #cedce4;

    .book-item {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      min-width: 255px;
      max-width: 255px;
      margin: 16px 0;
      height: fit-content;
      border-radius: 4px;
      overflow: hidden;
      cursor: pointer;

      .img-view {
        background: #eaf1f5;
        font-size: 0;
        text-align: center;
        height: 156px;
        padding: 8px 0;

        img {
          height: 100%;
          display: block;
          margin: 0 auto;
          border-radius: 4px;
          -webkit-box-sizing: border-box;
          box-sizing: border-box;
        }
      }

      .info-view {
        background: #f6f9fb;
        text-align: center;
        height: 108px;
        overflow: hidden;
        padding: 0 16px;

        h3 {
          color: #1c355a;
          font-weight: 500;
          font-size: 16px;
          line-height: 20px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          margin: 12px 0 8px;
        }

        .authors {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .translators {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          //   margin: 6px 0;
          white-space: nowrap;
        }
      }
    }
  }
}

.flex-view {
  display: flex;
}

.book-comment {
  .title {
    font-weight: 600;
    font-size: 14px;
    line-height: 22px;
    height: 22px;
    color: #152844;
    margin: 24px 0 12px;
  }

  .publish {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;

    .mine-img {
      -webkit-box-flex: 0;
      -ms-flex: 0 0 40px;
      flex: 0 0 40px;
      margin-right: 12px;
      border-radius: 50%;
      width: 40px;
      height: 40px;
    }

    .content-input {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      background: #f6f9fb;
      border-radius: 4px;
      height: 32px;
      line-height: 32px;
      color: #484848;
      padding: 5px 12px;
      white-space: nowrap;
      outline: none;
      border: 0px;
    }

    .send-btn {
      margin-left: 10px;
      background: #4684e2;
      border-radius: 4px;
      -webkit-box-flex: 0;
      -ms-flex: 0 0 80px;
      flex: 0 0 80px;
      color: #fff;
      font-size: 14px;
      text-align: center;
      height: 32px;
      line-height: 32px;
      outline: none;
      border: 0px;
      cursor: pointer;
    }
  }

  .tab-view {
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    font-size: 14px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    margin: 24px 0;

    .count-text {
      color: #484848;
      float: left;
    }

    .tab-box {
      color: #5f77a6;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;

      .tab-select {
        color: #152844;
      }

      span {
        cursor: pointer;
      }
    }

    .line {
      width: 1px;
      height: 12px;
      margin: 0 12px;
      background: #cedce4;
    }
  }
}

.comments-list {
  .comment-item {
    .flex-item {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      padding-top: 16px;

      .avator {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 40px;
        flex: 0 0 40px;
        width: 40px;
        height: 40px;
        margin-right: 12px;
        border-radius: 50%;
        cursor: pointer;
      }

      .person {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
      }

      .name {
        color: #152844;
        font-weight: 600;
        font-size: 14px;
        line-height: 22px;
        height: 22px;
        cursor: pointer;
      }

      .time {
        color: #5f77a6;
        font-size: 12px;
        line-height: 16px;
        height: 16px;
        margin-top: 2px;
      }

      .float-right {
        color: #4684e2;
        font-size: 14px;
        float: right;

        span {
          margin-left: 19px;
          cursor: pointer;
        }

        .num {
          color: #152844;
          margin-left: 6px;
          cursor: auto;
        }
      }
    }
  }
}

.comment-content {
  margin-top: 8px;
  color: #484848;
  font-size: 14px;
  line-height: 22px;
  padding-bottom: 16px;
  border-bottom: 1px dashed #cedce4;
  margin-left: 52px;
  overflow: hidden;
  word-break: break-word;
}

.infinite-loading-container {
  clear: both;
  text-align: center;
}
</style>
<!-- 目录的css -->
<style scoped>
.novel-directory {
  /* display: flex; */
  flex-wrap: wrap;
  padding-top: 10px;
}

.directory-row {
  flex: 1 0 33.33%;
  display: flex;
  justify-content: left;
  border-bottom: solid rgba(138, 100, 100, 0.386) 1px;
  margin-bottom: 5px;
}

.chapter-title {
  width: 30%;
  /* background-color: #f0f0f0; */
  padding: 10px;
  text-align: center;
  border-radius: 5px;
}

.chapter-title:hover {
  background-color: rgba(249, 26, 26, 0.144);
}
</style>