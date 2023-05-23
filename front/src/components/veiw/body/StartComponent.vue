<template>
  <div class="start-component" :style="{ backgroundImage: `url(${backgroundImage})` }" ref="startComponentRef">
    <div class="content">
      <h1 class="quote">{{ quote }}</h1>
      <button class="start-button" @click="hideComponent">开始</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundImage: require("../../../assets/imgs/PontdArcole_ZH-CN5348049357_1920x1080.jpg"),
      quote: "这里是引言",
    };
  },
  methods: {
    hideComponent() {
      this.$refs.startComponentRef.classList.add('slide-up');
      this.$emit('hidetrigger');
      // setTimeout(() => {
      //   this.$emit('hide');
      // }, 500);
    },
  },
};
</script>

<style scoped>
.start-component {
  /* position: fixed; */
  /* top:0; */
  width: 100vw;
  height: 100vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9998;
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
  animation: slideUp 0.5s forwards;
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
