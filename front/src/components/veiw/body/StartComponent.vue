<template>
  <div>
    <!-- <transition name="fade"> -->
      <div
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
        <button
          v-if="this.$store.state.isLogin"
          class="start-button"
          @click="hideComponent"
        >
          探索更多 >
        </button>
        <button v-else class="start-button" @click="hideComponent">
          开始探索 >
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
      backgroundImage: require("../../../assets/imgs/PontdArcole_ZH-CN5348049357_1920x1080.jpg"),
      showComponent: true,
      i: 0,
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
      }, 500);
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
  mounted() {
    // this.imgs = require
    //   .context("../../../assets/imgs/homepage/", false, /.jpg$/)
    //   .keys();
    // let index = Math.floor(Math.random() * this.imgs.length);
    // for (let i = 0; i < this.imgs.length; i++) {
    //   this.imgs[i] = require("../../../assets/imgs/homepage/" +
    //     this.imgs[i].substring(2));
    // }
    // for (let i = index; i < this.imgs.length; i++) {
    //   const cimg = new Image();
    //   cimg.src = this.imgs[i];
    // }
    // for (let i = 0; i < index; i++) {
    //   const cimg = new Image();
    //   cimg.src = this.imgs[i];
    // }
    // this.preloadImages(this.imgs, () => {
    //   this.startBackgroundRotation(0);
    // });
    // this.imgs.forEach((imagePath) => {
    //   const img = new Image();
    //   img.src = imagePath;
    // });
    // this.startBackgroundRotation(index);
  },
  created() {
    this.switch = Math.floor(Math.random() * this.strs.length);
    this.v = 1600 / this.strs[this.switch].length;
    this.imgs = require
      .context("../../../assets/imgs/homepage/", false, /.jpg$/)
      .keys();
    let index = Math.floor(Math.random() * this.imgs.length);
    for (let i = 0; i < this.imgs.length; i++) {
      this.imgs[i] = require("../../../assets/imgs/homepage/" +
        this.imgs[i].substring(2));
    }
    this.backgroundImage = this.backgroundImage = this.imgs[index];
    // let img = imgs[Math.floor(Math.random() * imgs.length)];
    // let path = ;
    // console.log(path);

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
  -webkit-line-clamp: 3; /* 这里是超出几行省略 */
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
  transition: all 0.5s;
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
  text-shadow: 1px 1px #0000004d;
}

.start-button {
  /* position: fixed; */
  /* position: fixed; */
  min-height: 20px;
  padding: 12px 24px;
  margin-top: 5%;
  background-color: #0000002b;
  color: #000;
  font-size: 18px;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  backdrop-filter: blur(3px) invert(5%);
  /* bottom: 200px; */
  transition: all 0.5s;
}
.start-button:hover {
  /* position: fixed; */
  backdrop-filter: blur(10px) invert(15%);
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
