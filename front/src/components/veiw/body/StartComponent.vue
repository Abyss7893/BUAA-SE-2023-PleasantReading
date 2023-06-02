<template>
  <div>
    <!-- <transition name="fade"> -->
    <div
      v-if="hidethis"
      class="start-component"
      :class="{ 'start-component-hidden': !showComponent }"
      :style="{
        backgroundImage: `url(${backgroundImage})`,
        marginTop: showComponent ? '' : 'calc(-106vh )',
      }"
      ref="startComponentRef"
    >
      <img src="../../../assets/logo-yixinyuedu.png" class="start-image" />
      <div style="height: 15%">
        <div class="hello-user">
          <div class="content">
            <h1 class="quote">
              {{ "你好，" + username }}
              <p class="startquote">{{ typewriter }}</p>
            </h1>
          </div>
        </div>
      </div>
      <div v-if="this.$store.state.isLogin" style="max-height: 300px">
        <slide-card> </slide-card>
      </div>
      <button class="start-button" @click="hideComponent">
        {{ this.$store.state.isLogin ? "探索更多" : "开始探索" }} >
      </button>
    </div>
    <!-- </transition> -->
  </div>
</template>
<script>
import SlideCard from "./other/SlideCard.vue";
// import store from "@/store";
// import { useStore } from "vuex";
export default {
  components: { SlideCard },
  data() {
    return {
      imgs: [],
      showLastRead: true,
      backgroundImage: null,
      showComponent: true,
      i: 0,
      hidethis: true,
      typewriter: "",
      strs: [
        "读书之法，在循序而渐进，熟读而精思。——朱熹",
        "立身以立学为先，立学以读书为本。——郑耕老",
        "不读书的人，思想就会停止。人都向往知识，一旦知识的渴望在他身上熄灭，他就不再成为人。——南森",
        "经验丰富的人读书用两只眼睛，一只眼睛看到纸面上的话，另一眼睛看到纸的背面。——歌德",
        "问渠那得清如许？为有源头活水来。——朱熹",
        "任何时候，我也不会满足，越是多读书，就越是深刻地感到不满足，越感到自己知识贫乏。科学是奥妙无穷的。——马克思",
        "喜爱读书，就等于把生活中寂寞无聊的时光换成巨大享受的时刻。——孟德斯鸠",
        "书籍便是这种改造灵魂的工具。人类所需要的，是富有启发性的养料。而阅读，则正是这种养料。——雨果",
        "读书时要深思多问。只读而不想，就可能人云亦云，沦为书本的奴隶；或者走马看花，所获甚微。——王梓坤",
      ],
      timer: 0,
      switch: 0,
      v: 10,
    };
  },
  methods: {
    hideComponent() {
      this.showComponent = !this.showComponent;
      // this.$refs.startComponentRef.classList.add('slide-up');
      setTimeout(() => {
        this.$emit("hide");
        setTimeout(() => {
          this.hidethis = false;
        }, 500);
      }, 50);
    },
    typing() {
      if (this.i <= this.strs[this.switch].length) {
        this.typewriter = this.strs[this.switch].slice(0, this.i++);
        this.timer = setTimeout(() => {
          this.typing();
        }, Math.floor(Math.random() * this.v + 20));
      } else {
        setTimeout(() => {
          this.typingreverse();
        }, 2000);
      }
    },
    changeShowLastRead() {
      console.log(this.showLastRead);
      this.showLastRead = !this.showLastRead;
    },
    typingreverse() {
      if (this.i > 0) {
        this.typewriter = this.strs[this.switch].slice(0, this.i--);
        this.timer = setTimeout(() => {
          this.typingreverse();
        }, Math.floor(Math.random() * this.v * 0.8));
      } else {
        this.switch++;
        this.switch = this.switch % this.strs.length;
        this.v = 1600 / this.strs[this.switch].length;
        this.typing();
      }
    },
    startBackgroundRotation(index) {
      // console.log(this.imgs[index]);
      this.backgroundImage = this.backgroundImage = this.imgs[index];
      setInterval(() => {
        index = (index + 1) % this.imgs.length;
        this.backgroundImage = this.imgs[index];
        // console.log(this.imgs[index]);
        console.log(this.imgs);
      }, 10000);
    },
    preloadImages(imagePaths, callback) {
      let loadedCounter = 0;
      const imageCount = imagePaths.length;

      // 定义加载完成的回调函数
      function imageLoaded() {
        loadedCounter++;
        if (loadedCounter === imageCount) {
          // 所有图片加载完成后调用回调函数
          console.log("Loading", loadedCounter);
          callback();
        }
      }

      // 创建 Image 对象并设置加载完成的回调函数
      imagePaths.forEach((imagePath) => {
        const img = new Image();
        img.onload = imageLoaded;
        img.onerror = imageLoaded;
        img.src = imagePath;
      });
    },
    randomBg(index) {
      this.backgroundImage = this.imgs[index];
      let index2 = Math.floor(Math.random() * this.imgs.length);
      while (index2 == index) {
        index2 = Math.floor(Math.random() * this.imgs.length);
      }
      index = index2;
      const img = new Image();
      img.onload = () => {};
      img.onerror = () => {};
      img.src = this.imgs[index];

      setTimeout(() => {
        this.randomBg(index);
      }, 5000);
    },
  },
  computed: {
    username() {
      // const store = this.$store.state;
      console.log("是否登录");
      console.log(this.$store.state.isLogin);
      return this.$store.state.isLogin
        ? this.$store.state.userInfo.username
        : "读者";
    },
  },
  created() {
    this.switch = Math.floor(Math.random() * this.strs.length);
    this.v = 1600 / this.strs[this.switch].length;
    this.imgs = [
      "https://i.imgloc.com/2023/05/29/VtxwjH.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxlVF.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtx0oZ.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxkR8.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxWU5.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxnLy.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxUg3.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxDCv.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtx4QU.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtxy6p.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxfbL.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxVVk.jpeg",
      "https://i.imgloc.com/2023/05/29/VtxZSx.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtgu3a.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgqUw.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgQKz.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtg1Xq.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgaCb.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgP1d.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgM6V.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgLbN.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgKio.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtg9SA.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtgv3c.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgsDJ.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgSKt.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtg5XX.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtgh0P.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgG1C.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgFzE.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtg6OQ.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgziH.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgE5F.jpeg",
      "https://i.imgloc.com/2023/05/29/Vtg73Z.jpeg",
      "https://i.imgloc.com/2023/05/29/VtgxD8.jpeg",
    ];

    // for (let i = 0; i < this.imgs.length; i++) {
    //   this.imgs[i] = require("../../../assets/imgs/homepage/" +
    //     this.imgs[i].substring(2));
    // }

    // let img = imgs[Math.floor(Math.random() * imgs.length)];
    // let path = ;
    // console.log(path);
    let index = Math.floor(Math.random() * this.imgs.length);
    this.randomBg(index);
    this.typing();
  },
};
</script>

<style scoped>
.start-image {
  max-width: 32%;
  /* backdrop-filter: blur(3px) invert(5%); */
  /* border-radius: 30px; */
  /* box-shadow:inset(0.5, 0.5, 0.5, 0 ); */
  /* border: solid rgba(212, 184, 6, 0.164) 1px; */
  transition: all 0.5s;
}

.start-image:hover {
  scale: 1.1;
  max-width: 32%;
  backdrop-filter: blur(3px) invert(5%);
  border-radius: 30px;
  /* box-shadow:inset(0.5, 0.5, 0.5, 0 ); */
  border: solid rgba(212, 184, 6, 0.164) 1px;
}

.startquote {
  font-family: kaiti;
  max-width: 700px;
  color: #e2e6ec;
  white-space: normal;
  max-height: 200px;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  /* 这里是超出几行省略 */
  overflow: hidden;
  /* filter: invert(100%); */
  /* background: inherit; */
  background-clip: text;
  -webkit-background-clip: text;
  /* color: transparent; */
  /* filter: grayscale(1) contrast(9); */
  /* backdrop-filter: blur(10px); */
}

.start-component {
  margin-top: -3%;
  /* position: fixed; */
  flex-direction: column;
  width: auto;
  height: 106vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  transition: margin-top 0.5s, background-image 2s;
  /* transition: background-image 2s; */
}

.start-component-hidden {
  margin-top: -100px;
}

.content {
  margin: 10px;
  /* backdrop-filter: blur(2px); */
  text-align: center;
}

.hello-user {
  min-height: 148px;
  min-width: 720px;
  transition: all 0.5s;
  border-radius: 10px;
}

.hello-user:hover {
  border: solid rgba(212, 184, 6, 0.164) 1px;
  backdrop-filter: blur(3px) invert(10%);
}

.quote {
  font-size: 24px;
  color: #fff;
  margin-bottom: 20px;
  max-height: 100px;
  text-shadow: 2px 1px #000000b5;
}

.start-button {
  min-height: 20px;
  padding: 12px 24px;
  margin-top: 5%;
  background-color: #00000073;
  color: #d7d5d5;
  font-size: 18px;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  transition: all 0.5s;
  z-index: 10;
}

.start-button:hover {
  /* position: fixed; */
  backdrop-filter: blur(5px) invert(5%);
  scale: 1.1;
}

.slide-up {
  transition: 0.5s forwards;
}

@keyframes slideUp {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(-100%);
  }
}
</style>
