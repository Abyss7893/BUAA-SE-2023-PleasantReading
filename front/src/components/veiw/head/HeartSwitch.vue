<template>
  <label class="box">
    <!-- 复选框，有选中状态 -->
    <input type="checkbox" v-model="this.switchchange">

    <!-- 心形图标 -->
    <svg viewBox="0 0 33 23" fill="pink">
      <path
        d="M23.5,0.5 C28.4705627,0.5 32.5,4.52943725 32.5,9.5 C32.5,16.9484448 21.46672,22.5 16.5,22.5 C11.53328,22.5 0.5,16.9484448 0.5,9.5 C0.5,4.52952206 4.52943725,0.5 9.5,0.5 C12.3277083,0.5 14.8508336,1.80407476 16.5007741,3.84362242 C18.1491664,1.80407476 20.6722917,0.5 23.5,0.5 Z">
      </path>
    </svg>
  </label>
</template>

<script>
export default {
  props: {
    switch: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      switchchange: this.switch,
    }
  },
  watch: {
    switchchange(val) {
      this.$emit('swithChange', val)
    }
  }
};
</script>
<style lang="scss" scoped>
.box {
  /* 整个父盒子区域都可以点，是个小手 */
  cursor: pointer;
  /* 过渡动画时间，主要是按下缩小一圈 */
  transition: transform 0.2s;
  margin-right: 24px;
  position: relative;
}

.box:active {
  /* 点击时，缩小一圈 */
  transform: scale(0.95);
}

.box svg {
  /* 中间心形图标的宽高，撑开整个开关区域 */
  width: 60px;
  height: 45px;
  /* background-color: skyblue; */

  /* 中间填充颜色 */
  fill: #ffffff;
  /* 描边颜色，描边头是圆润的 */
  stroke: #d6d6ee;
  stroke-linejoin: round;

  /* 过渡动画时间 */
  transition: all 0.4s;
}

.box input:checked+svg {
  /* 开关打开时修改心形图标颜色 */
  fill: #f8b2b2;
  stroke: #f8b2b2;
}

.box input {
  /* 去除默认复选框样式 */
  appearance: none;

  /* 中间滑动圆圈的宽高，简单白色背景 */
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #ffffff;
  /* 灰色阴影 */
  box-shadow: 0 0.5px 2px rgba(0, 0, 0, 0.2);
  /* 鼠标小手 */
  cursor: pointer;

  /* 初始位置，具体值要根据实际情况微调 */
  position: absolute;
  top: 2.5px;
  left: 1.5px;

  /* 开关未打开时，默认使用关闭的动画，然后停在初始位置 */
  animation: animate-off 0.4s linear forwards;
}

.box input:checked {
  /* 开关打开时，使用打开动画，然后停在打开的位置 */
  animation: animate 0.4s linear forwards;
}

@keyframes animate {

  /* 动画就是简单的位置变换，要根据情况调整 */
  0% {
    top: 3.75px;
    left: 2.25px;
  }

  25% {
    top: 8.25px;
    left: 7.5px;
  }

  50% {
    top: 10.5px;
    left: 15px;
    /* 到正中间时圆大一小圈 */
    transform: scale(1.05);
  }

  75% {
    top: 8.25px;
    left: 22.5px;
  }

  100% {
    top: 3.75px;
    left: 27.75px;
  }
}

@keyframes animate-off {

  /* 关闭的动画就是反着来 */
  0% {
    top: 3.75px;
    left: 27.75px;
  }

  25% {
    top: 8.25px;
    left: 22.5px;
  }

  50% {
    top: 10.5px;
    left: 15px;
    transform: scale(1.05);
  }

  75% {
    top: 8.25px;
    left: 7.5px;
  }

  100% {
    top: 3.75px;
    left: 2.25px;
  }
}
</style>