<!-- 头部的导航栏 -->
<template>
  <div class="head-nav">
    <ul>
      <div class="slider"></div>
      <li @mouseover="slideHere" ref="firstli" @mouseout="slideAway">
        <a href="#">首页</a>
      </li>
      <li @mouseover="slideHere" @mouseout="slideAway"><a href="#">全部作品</a></li>
      <li @mouseover="slideHere" @mouseout="slideAway"><a href="#">作品排行</a></li>
      <li @mouseover="slideHere" @mouseout="slideAway"><a href="#">完本作品</a></li>
      <li @mouseover="slideHere" @mouseout="slideAway"><a href="#">我的书架</a></li>
      <li @mouseover="slideHere" @mouseout="slideAway"><a href="#">我的笔记</a></li>

    </ul>
  </div>
</template>
<script>
import "css/head/headnav.css"

export default {
  name: 'Head_Nav',
  components: {

  },
  data() {
    return {
      naviLoccation: null,
      slider: null,
      screenWidth: null,
    }
  },
  watch: {
    screenWidth: {
      handler: function () {
        this.naviLoccation = this.$refs.firstli.getBoundingClientRect()
        this.slideAway();
      },
    },
  },
  mounted() {
    this.screenWidth = document.body.clientWidth
    window.onresize = () => {
      return (() => {
        this.screenWidth = document.body.clientWidth
      })()
    }
    this.slider = document.querySelector('.slider')
    this.naviLoccation = this.$refs.firstli.getBoundingClientRect()
    this.slider.style.height = this.naviLoccation.height + "px"
    this.slider.style.width = this.naviLoccation.width + "px"
    this.slider.style.left = this.naviLoccation.left + "px"
  },
  methods: {
    slideHere(event) {
      const rect = event.target.getBoundingClientRect()
      this.slider.style.width = rect.width + "px"
      this.slider.style.left = rect.left + "px"
      this.slider.style.height = rect.height + "px"
    },
    slideAway() {
      // console.log(this.naviLoccation.width)
      this.slider.style.width = this.naviLoccation.width + "px"
      this.slider.style.left = this.naviLoccation.left + "px"
      this.slider.style.height = this.naviLoccation.height + "px"
    }
  }
}
</script>