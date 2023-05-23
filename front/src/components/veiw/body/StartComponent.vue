<template>
  <div>
    <div
      class="start-component"
      :class="{ 'start-component-hidden': !showComponent }"
      :style="{
        backgroundImage: `url(${backgroundImage})`,
        marginTop: showComponent ? '' : 'calc(-104vh )',
      }"
      ref="startComponentRef"
    >
      <div class="content">
        <h1 class="quote">{{ quote }}</h1>
        <button class="start-button" @click="hideComponent">开始</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundImage: require("../../../assets/imgs/PontdArcole_ZH-CN5348049357_1920x1080.jpg"),
      quote: "这里是引言",
      showComponent: true,
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
  },
  created() {
    let imgs = require
      .context("../../../assets/imgs/homepage/", false, /.jpg$/)
      .keys();
    let img = imgs[Math.floor(Math.random() * imgs.length)];
    // let path = ;
    // console.log(path);
    this.backgroundImage = require("../../../assets/imgs/homepage/"+img.substring(2));
  
  },
};
</script>

<style scoped>
.start-component {
  margin-top: -3%;
  /* position: fixed; */
  width: 100vw;
  height: 104vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  transition: all 0.5s;
}
.start-component-hidden {
  margin-top: -100px;
}

.content {
  text-align: center;
}

.quote {
  font-size: 24px;
  color: #fff;
  margin-bottom: 20px;
}

.start-button {
  padding: 12px 24px;
  background-color: #fff;
  color: #000;
  font-size: 18px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
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
