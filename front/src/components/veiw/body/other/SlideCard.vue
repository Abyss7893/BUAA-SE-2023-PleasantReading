<template>
  <div>
    <div>
      <h1 class="quote" style="text-align: center">最近阅读</h1>
      <div style="min-height: 400px">
        <transition name="el-zoom-in-top">
          <div v-if="isshow">
            <transition name="fade">
              <div
                @touchend="end"
                @touchstart="start"
                @touchmove="move"
                class="swiper"
              >
                <div
                  @click="chooseItem(item, index)"
                  v-for="(item, index) in imgs"
                  :style="config5[index]"
                  :key="item.cover"
                  @mouseover="touchcenter(config5[index].id === 'center')"
                  @mouseout="leavecenter(config5[index].id === 'center')"
                  style="
                    /* background-color: red; */
                    width: 150px;
                    height: 208px;
                    border-radius: 20px;
                  "
                  :class="{
                    'hover-effect': config5[index].id === 'center',
                    'other-hover-effect': config5[index].id !== 'center',
                  }"
                  class="card-control"
                >
                  <img
                    :src="item.cover"
                    class="card-img"
                    style="z-index: 4 !important"
                  />
                  <!-- <div class="wordblock"
            style="z-index: 9999;"> -->
                  <el-collapse-transition>
                    <el-tooltip
                      class="box-item"
                      effect="dark"
                      :content="item.id"
                      placement="right"
                    >
                      <!-- <el-button>right</el-button> -->

                      <router-link :to="{ path: '/book/' + item.bookId }">
                        <p
                          v-if="config5[index].id === 'center'"
                          style="
                            /* position: absolute; */
                            /* color: rgba(126, 84, 84, 0.582); */
                            color: rgba(202, 197, 197, 0);
                            /* left: 10%; */
                            text-align: center;
                            margin: 3px;
                            bottom: 50px;
                            transition: ease-in-out 0.2s;
                            z-index: 3 !important;
                            -webkit-user-select: none;
                            -moz-user-select: none;
                            -ms-user-select: none;
                            user-select: none;
                            white-space: normal;
                            word-break: break-all;
                            text-overflow: ellipsis;
                            display: -webkit-box;
                            -webkit-box-orient: vertical;
                            -webkit-line-clamp: 1;
                            /* 这里是超出几行省略 */
                            overflow: hidden;
                          "
                          class="content-effect"
                        >
                          {{ item.id }}
                        </p>
                      </router-link>
                    </el-tooltip>
                  </el-collapse-transition>
                  <el-collapse-transition>
                    <el-tooltip
                      class="box-item"
                      effect="dark"
                      :content="item.chapter"
                      placement="right"
                    >
                      <router-link
                        :to="{
                          path: '/reader/' + item.bookId + '/' + item.chapterid,
                        }"
                      >
                        <p
                          v-if="config5[index].id === 'center'"
                          style="
                            /* position: absolute; */
                            bottom: 30px;
                            /* margin-left: 10px; */
                            left: 10%;
                            color: rgba(216, 212, 203, 0);
                            text-align: center;
                            font-family: kaiti;
                            margin: 3px;
                            transition: 0.2s;
                            z-index: 3 !important;
                            white-space: normal;
                            word-break: break-all;
                            text-overflow: ellipsis;
                            display: -webkit-box;
                            -webkit-box-orient: vertical;
                            -webkit-line-clamp: 3;
                            /* 这里是超出几行省略 */
                            overflow: hidden;
                          "
                          class="content-effect"
                        >
                          {{ item.chapter }}
                        </p>
                      </router-link>
                    </el-tooltip>
                  </el-collapse-transition>
                  <!-- </div> -->
                  <!-- <span>{{ item.dindex }}</span> -->
                </div>
              </div>
            </transition>
          </div></transition
        >
        <!-- <div style="display: flex; align-items: center">
      <h1 @click="prev">上一个</h1>
      |
      <h1>当前：{{ centerInfo.id }}</h1>
      |
      <h1 @click="next">下一个</h1>
    </div> -->
      </div>
    </div>
  </div>
</template>
    <script>
// import { da } from 'element-plus/es/locale';
// import { fa } from "element-plus/es/locale";
// import BookCard from "../mybooks/BookCard.vue";
import { getRecent, getBookList, getBookDetiles } from "@/api/api";
export default {
  // components: { BookCard },
  //   name: "zt",
  data() {
    return {
      isshow: false,
      showLastRead: true,
      showInfo: false,
      loading: true,
      currentIndex: 3, //当前中间imgs数组中index
      centerInfo: "", // 当前中间信息
      startX: "",
      endX: "",

      // imgs: [
      //   {
      //     id: "莱因哈特1",
      //     index: 0,
      //     dindex: 0,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888260036&di=875bc88905bf4b6923784df1589edb0b&imgtype=0&src=http%3A%2F%2Fi-1.itobike.com%2F2017%2F5%2F26%2Ff6038942-393f-441e-9380-a2f1607c3385.jpg",
      //   },
      //   {
      //     id: "安娜2",
      //     index: 1,
      //     dindex: 1,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888297322&di=9d5d97f952329ccf2277b2033b129d5d&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201803%2F28%2F20180328101238_VHiji.jpeg",
      //   },
      //   {
      //     id: "卢西奥3",
      //     index: 2,
      //     dindex: 2,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573483062&di=9d6983ba28c123896b27148e313ada65&imgtype=jpg&er=1&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201608%2F15%2F20160815133037_4YAfh.jpeg",
      //   },
      //   {
      //     id: "DVA4",
      //     index: 3,
      //     dindex: 3,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888405708&di=3381891cd042db432083ed2446ddf446&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201805%2F06%2F20180506201144_JPTd3.thumb.700_0.jpeg",
      //   },
      //   {
      //     id: "莫伊拉5",
      //     index: 4,
      //     dindex: 4,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888441984&di=47544529365104e11276d639838741c3&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201801%2F06%2F20180106221938_58EGv.thumb.224_0.jpeg",
      //   },
      //   {
      //     id: "裂空6",
      //     index: 5,
      //     dindex: 5,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888482891&di=5416c6abf187547cd329377dc1092fff&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201610%2F20%2F20161020175323_auiK8.thumb.700_0.jpeg",
      //   },
      //   {
      //     id: "麦克雷7",
      //     index: 6,
      //     dindex: 6,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572888500984&di=f415feaef2c02b497e9d3801743b8e49&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201711%2F26%2F20171126191812_4x8RV.thumb.700_0.jpeg",
      //   },
      //   {
      //     id: "士兵76  8",
      //     index: 7,
      //     dindex: 7,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573056788040&di=dbf1954ad8ba1bee16afd9f47d763512&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201704%2F24%2F20170424202013_hveir.jpeg",
      //   },
      //   {
      //     id: "狂鼠9",
      //     index: 8,
      //     dindex: 8,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "http://ztd00.photos.bdimg.com/ztd/w=700;q=50/sign=ea29fa95c13d70cf4cfaa80dc8e7a03d/42166d224f4a20a4d334946b98529822720ed070.jpg",
      //   },
      //   {
      //     id: "死神 10",
      //     index: 9,
      //     dindex: 9,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "http://www.agri35.com/UploadFiles/img_2_4163694432_214245738_26.jpg",
      //   },
      //   {
      //     id: "禅雅塔 11",
      //     index: 10,
      //     dindex: 10,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "http://pic2.zhimg.com/v2-1c9b73f260ea2652dcdedfc782fde90d_b.jpg",
      //   },
      //   {
      //     id: "黑百合 12",
      //     index: 11,
      //     dindex: 11,
      //     cover: require("../../../../assets/imgs/bookcv.png"),
      //     // "http://b-ssl.duitang.com/uploads/item/201710/14/20171014134122_KmPQy.jpeg",
      //   },
      // ],
      imgs: [],
      data: [],
      previous: 0,
      config5: [
        {
          id: "-A",
          position: "absolute",
          width: "22%",
          height: "72%",
          // top: "-7%",
          top: "-9px",
          left: "-22%",
          opacity: 0,
          zIndex: 2,
          transition: ".4s",
        },
        {
          id: "A",
          position: "absolute",
          width: "22%",
          height: "72%",
          // top: "-5%",
          top: "-6px",
          left: "0%",
          opacity: 1,
          zIndex: 4,
          transition: ".4s",
        },
        {
          id: "B",
          position: "absolute",
          width: "28%",
          height: "82%",
          // top: "-3%",
          top: "-3px",
          left: "13%",
          opacity: 1,
          zIndex: 6,
          transition: ".4s",
        },
        {
          id: "center",
          position: "absolute",
          width: "45%",
          height: "100%",
          top: "0px",
          left: "50%",
          marginLeft: "-22.5%",
          opacity: 1,
          zIndex: 8,
          transition: ".4s",
          border: "4px",
        },
        {
          id: "D",
          position: "absolute",
          width: "28%",
          height: "82%",
          // top: "-3%",
          top: "-3px",
          left: "44%",
          opacity: 1,
          zIndex: 7,
          transition: ".4s",
        },
        {
          id: "E",
          position: "absolute",
          width: "22%",
          height: "72%",
          // top: "-5%",
          top: "-6px",
          left: "60%",
          opacity: 1,
          zIndex: 5,
          transition: ".4s",
        },
        {
          id: "E+",
          position: "absolute",
          width: "22%",
          height: "72%",
          // top: "-7%",
          top: "-9px",
          left: "81%",
          opacity: 0,
          zIndex: 3,
          transition: ".4s",
        },
      ],

      mode: 0,
    };
  },
  methods: {
    touchcenter(bool) {
      if (bool) {
        this.showLastRead = false;

        for (let cfg of this.config5) {
          if (cfg.id === "center") cfg.left = "50%";
          else if (cfg.id === "-A") {
            cfg.left = "-160%";
            cfg.opacity = this.mode == 7 ? 1 : 0;
          } else if (cfg.id === "A") cfg.left = "-100%";
          else if (cfg.id === "B") cfg.left = "-40%";
          else if (cfg.id === "D") cfg.left = "94%";
          else if (cfg.id === "E") cfg.left = "152%";
          else if (cfg.id === "E+") {
            cfg.left = "210%";
            cfg.opacity = this.mode == 7 ? 1 : 0;
          }
        }

        this.$emit("showLastRead");
      }

      // var ccfg;
      // for (let cfg of this.config5) {
      //   if (cfg.id === "center") ccfg = cfg;
      // }
      // if (bool) {
      //   for (let cfg of this.config5) {
      //     let diff = parseInt(cfg.left, 10) - parseInt(ccfg.left, 10);
      //     cfg.left = parseInt(ccfg.left, 10) + diff * 3 + "%";
      //   }
      // }
    },
    leavecenter(bool) {
      if (bool) {
        this.showLastRead = true;
        this.showInfo = false;
        for (let cfg of this.config5) {
          if (cfg.id === "center") cfg.left = "50%";
          else if (cfg.id === "-A") {
            cfg.left = "-22%";
            cfg.opacity = 0;
          } else if (cfg.id === "A") cfg.left = "0%";
          else if (cfg.id === "B") cfg.left = "13%";
          else if (cfg.id === "D") cfg.left = "44%";
          else if (cfg.id === "E") cfg.left = "60%";
          else if (cfg.id === "E+") {
            cfg.left = "81%";
            cfg.opacity = 0;
          }
        }

        this.$emit("showLastRead");
      }
    },
    // 获取数据
    async getData() {
      this.$nextTick(() => {
        this.loading = false;
      });
    },

    // 滑动上一个
    prev() {
      // this.imgs.unshift(this.imgs.pop());
      this.config5.push(this.config5.shift());
      this.currentIndex = this.currentIndex - 1;
      if (this.currentIndex < 0) {
        this.currentIndex = this.imgs.length - 1;
      }
      this.centerCard();
      this.centerIndex("prev");
    },
    // 滑动下一个
    next() {
      // this.imgs.push(this.imgs.shift());
      this.config5.unshift(this.config5.pop());
      this.currentIndex = this.currentIndex + 1;
      if (this.currentIndex > this.imgs.length - 1) {
        this.currentIndex = 0;
      }
      this.centerCard();
      this.centerIndex("next");
      // console.log(this.currentIndex);
    },
    // 开始移动端滑动屏幕
    start(event) {
      this.startX = event.changedTouches[0].clientX;
      this.startY = event.changedTouches[0].clientY;
    },
    // 连续滑动
    move(event) {
      this.endY = event.changedTouches[0].clientY;
      this.endX = event.changedTouches[0].clientX;
      this.stopDefault(event);
      // 如果是滑动，注解（223行到231行）这段。如果是连续滑动，放开（223行到231行）注解
      this.interval = this.endX - this.startX;
      if (this.interval > 40) {
        this.startX = this.endX;
        this.prev();
      }
      if (this.interval < -40) {
        this.startX = this.endX;
        this.next();
      }
    },
    // 滑动
    end() {
      // 如果是滑动，放开（236行到238行）的注解。如果是连续滑动，注解（236行到238行）
      // this.endY = event.changedTouches[0].clientY;
      // this.endX = event.changedTouches[0].clientX;
      // this.formatSwiper();
    },
    formatSwiper() {
      if (this.startX > this.endX) {
        console.log("左边滑动");
        if (this.startX > this.endX + 40) {
          this.next();
        }
      } else {
        console.log("右边滑动");
        if (this.endX > this.startX + 40) {
          this.prev();
        }
      }
    },
    // 阻止touchmove的横向默认事件（ios快捷操作会关闭页面）
    stopDefault(event) {
      let differenceY = this.endY - this.startY;
      let differenceX = this.endX - this.startX;
      if (Math.abs(differenceX) > Math.abs(differenceY)) {
        event.preventDefault();
      }
    },
    // 当前imgs在位置上的index（并非img数组的index）
    centerIndex(val) {
      if (val == "prev") {
        for (let val of this.imgs) {
          if (val.index == this.imgs.length - 1) {
            val.index = 0;
          } else {
            val.index = val.index + 1;
          }
        }
      } else {
        for (let val of this.imgs) {
          if (val.index == 0) {
            val.index = this.imgs.length - 1;
          } else {
            val.index = val.index - 1;
          }
        }
      }
    },
    // 点击
    chooseItem(item) {
      let cycles = item.index;
      console.log("this :" + cycles);
      if (cycles == 0 || cycles == 6) return;
      if (this.mode == 3) {
        if (cycles == 1 || cycles == 5) return;
      }
      if (this.mode == 1) {
        if (cycles == 1 || cycles == 5 || cycles == 2 || cycles == 4) return;
      }
      console.log(item);
      // let halfindex=0;
      // if(this.mode == 7) halfindex = 3;
      // else if(this.mode == 5) halfindex = 2;
      // else if(this.mode == 3) halfindex = 1;

      if (item.opacity == 0) return;

      if (item.index < 3) {
        for (let i = 0; i < 3 - cycles; i++) {
          console.log(item.index);
          this.prev();
        }
      } else if (item.index > 3) {
        for (let i = -1; i < item.index - 3; i++) {
          this.next();
        }
      } else if (item.index == 3) {
        console.log("投票");
      }
    },
    // 计算中间卡片信息
    centerCard() {
      this.centerInfo = this.imgs[this.currentIndex];
      this.$emit("centerInfo", this.centerInfo);
      // this.$emit('centerInfo', this.centerInfo);
      // console.log(this.imgs[2].id);
    },

    addCardStyle() {
      if (this.imgs.length > 7) {
        let addtime = this.imgs.length - 7;
        for (let i = 0; i < addtime; i++) {
          console.log("add");
          this.config5.push({
            id: "center",
            position: "absolute",
            width: "45%",
            height: "100%",
            top: "0px",
            left: "50%",
            marginLeft: "-22.5%",
            opacity: 0,
            transition: ".1s",
          });
        }
      }
    },
    deepCopy(x) {
      return {
        id: x.id,
        bookId: x.bookId,
        cover: x.cover,
        // dindex: book.dindex,
        index: x.index,
        chapterid: x.chapterid,
        chapter: x.chapter,
      };
    },
    getweekpoplist(weekpoplist) {
      let optheon = {
        page: "1",
        order: "weekpop",
      };
      getBookList(optheon).then((data) => {
        var list = data.books;
        for (let i = 0; i < list.length; i++) {
          getBookDetiles(list[i]).then((book) => {
            weekpoplist.push({
              name: book.title,
              id: book.id,
              author: book.author,
              cover: book.cover,
              state: [
                book.vip ? "VIP" : "免费",
                book.category,
                this.getSimpleSize(book.cnt),
              ],
            });
          });
        }
      });
    },
    setData() {
      for (var i = 0; i < 7; i++) {
        this.imgs.push({
          id: "",
          bookId: 0,
          cover: "",
          // dindex: book.dindex,
          index: 0,
          chapterid: 0,
          chapter: "",
        });
      }
      // getRecent().then()
      getRecent().then((response) => {
        // if (response.status == 200) {

        var data = [];

        if (response.status == 200) {
          data = response.data.list;
          // data =data.slice(0,3);
          // console.log("data", data);
        }
        let i = 0;
        // if (data.length > 0) {
        // console.log("response", data);
        console.log("book", i);
        for (let book of data) {
          this.imgs[i] = {
            id: book.name,
            bookId: book.bookID,
            cover: "http://154.8.183.51/media/" + book.img,
            // dindex: book.dindex,
            index: i,
            chapterid: book.chapter,
            chapter: book.title,
          };
          i++;
          // console.log("book", i);
        }
        // }
        console.log("imgs", this.imgs);
        if (i >= 7) {
          this.mode = 7;
          this.imgs = this.imgs.slice(0, 7);
          // console.log("end", this.imgs);
          for (let i = 0; i < 3; i++) this.prev();
          setTimeout(() => (this.isshow = true), 100);
        } else {
          let optheon = {
            page: "1",
            order: "weekpop",
          };
          getBookList(optheon).then((tdata) => {
            var list = tdata.books;
            var t = i;
            for (let j = 0; j < 7 - t; j++) {
              getBookDetiles(list[j]).then((book) => {
                this.imgs[i] = {
                  id: book.title,
                  bookId: book.id,

                  cover: book.cover,
                  index: i++,
                  chapterid: 1,
                  chapter: "本周推荐",
                };

                // console.log(i, this.imgs);
                if (i == 7) {
                  this.mode = 7;
                  // console.log(this.mode, this.imgs);

                  // this.data.push(...this.imgs);
                  this.imgs = this.imgs.slice(0, 7);
                  // console.log("end", this.imgs);
                  for (let i = 0; i < 3; i++) this.prev();
                  this.isshow = true;

                  return;
                }
              });
            }
          });
        }
      });
    },
    initThis() {},
  },
  created() {
    this.setData();
    console.log(this.imgs);
    this.getData();

    this.centerCard(); // 获取中间卡片信息
    this.addCardStyle(); // 加入样式位置的index

    // for (let _i = 0; _i < 3; _i++) {
    //   this.prev();
    // }
  },
};
</script>
    
    <style lang="less" scoped>
.card-control {
  .card-img {
    // display:inline-block;
    width: 150px;
    height: 208px;
    max-width: 150px;
    max-height: 208px;
    border-radius: 20px;
    z-index: 50 !important;
    // width: 100px;
    // height: 144px;
    transition: all 0.5s;
    border-left: solid rgba(187, 183, 183, 0.361);
    border-top: solid rgba(130, 127, 127, 0.425);
    -webkit-filter: drop-shadow(
      10px 10px 10px rgba(0, 0, 0, 0.5)
    ); /*考虑浏览器兼容性：兼容 Chrome, Safari, Opera */
    filter: drop-shadow(10px 10px 10px rgba(0, 0, 0, 0.5));
  }
}
.other-hover-effect:hover {
  .card-img {
    margin-top: -50px;
    z-index: 5;
  }
}
// .hover-effect {
//   transition: all 0.5s;
//   .content-effect {
//     // transition: all 0.5s;
//     color: rgb(90, 52, 52);
//   }
// }

.hover-effect:hover {
  /* 添加您想要的hover效果样式 */
  /* 例如修改背景色 */
  background-color: rgba(5, 5, 5, 0.276) !important;
  backdrop-filter: blur(5px) !important;

  scale: 1.2;
  /* 或者修改文本颜色 */
  color: rgb(7, 7, 7);
  top: 40px !important;
  .card-img {
    margin-top: -100px;
    max-width: 150px !important;
    max-height: 208px !important;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    border-bottom: solid salmon 2px;
  }

  .content-effect {
    // transition: all 0.5s;
    color: rgb(202, 197, 197) !important;
  }
}
.card-item {
  width: 200px;
  height: 288px;
  // border-radius: 20px;
  backdrop-filter: blur(3px) invert(5%);
}

// .card-img {
//   border-radius: 10px;
//   // width: 100px;
//   // height: 144px;
//   transition: all 0.5s;
//   border-left: solid rgba(187, 183, 183, 0.361);
//   border-top: solid rgba(130, 127, 127, 0.425);
//   -webkit-filter: drop-shadow(
//     10px 10px 10px rgba(0, 0, 0, 0.5)
//   ); /*考虑浏览器兼容性：兼容 Chrome, Safari, Opera */
//   filter: drop-shadow(10px 10px 10px rgba(0, 0, 0, 0.5));
// }
// .card-img:hover {
// z-index: 9999;
// margin-top: -50px;
// }
.swiper {
  //   width: 100%;
  align-items: center;
  margin: auto;
  margin-top: 30px;
  max-width: 288px;
  min-width: 288px;
  max-width: 288px;
  //   border: 1px red solid;
  height: 400px;
  position: relative;
  //   overflow: hidden;
  div {
    opacity: 0;
  }
}
.quote {
  font-size: 24px;
  color: #fff;
  margin-bottom: 20px;
  max-height: 100px;
  text-shadow: 1px 1px #0000004d;
  // transition: 0.5s;
}
</style>
    