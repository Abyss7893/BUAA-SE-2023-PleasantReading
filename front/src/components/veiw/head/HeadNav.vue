<!-- 头部的导航栏 -->
<template>
  <div class="head-nav">
    <ul>
      <div class="slider"></div>
      <li
        navi-id="1"
        @mouseover="slideHere"
        ref="firstli"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">首页</a>
      </li>
      <li
        navi-id="2"
        @mouseover="slideHere"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">全部作品</a>
      </li>
      <li
        navi-id="3"
        @mouseover="slideHere"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">作品排行</a>
      </li>
      <li
        navi-id="4"
        @mouseover="slideHere"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">完本作品</a>
      </li>
      <!-- <router-link :to="{ name: 'mybook' }"> -->
      <li
        navi-id="5"
        @mouseover="slideHere"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">我的书架</a>
      </li>
      <!-- </router-link> -->
      <li
        navi-id="6"
        @mouseover="slideHere"
        @mouseout="slideAway"
        @click="storeNavi"
      >
        <a href="#">我的笔记</a>
      </li>
    </ul>
  </div>
</template>
<script>
import "css/head/headnav.css";

export default {
  name: "Head_Nav",
  components: {},
  data() {
    return {
      naviLoccation: null,
      slider: null,
      screenWidth: null,
    };
  },
  watch: {
    screenWidth: {
      handler: function () {
        let id = this.$store.state.navigationLoc;
        this.naviLoccation = document
          .querySelector(`li[navi-id="${id}"]`)
          .getBoundingClientRect();
        this.slideAway();
      },
    },
  },
  mounted() {
    this.screenWidth = document.body.clientWidth;
    window.onresize = () => {
      return (() => {
        this.screenWidth = document.body.clientWidth;
      })();
    };
    this.slider = document.querySelector(".slider");
    let id = this.$store.state.navigationLoc;
    this.naviLoccation = document
      .querySelector(`li[navi-id="${id}"] a`)
      .getBoundingClientRect();
    this.slider.style.height = this.naviLoccation.height + "px";
    this.slider.style.width = this.naviLoccation.width + "px";
    this.slider.style.left = this.naviLoccation.left + "px";
  },
  methods: {
    slideHere(event) {
      const rect = event.target.getBoundingClientRect();
      this.slider.style.width = rect.width + "px";
      this.slider.style.left = rect.left + "px";
      this.slider.style.height = rect.height + "px";
    },
    slideAway() {
      this.slider.style.width = this.naviLoccation.width + "px";
      this.slider.style.left = this.naviLoccation.left + "px";
      this.slider.style.height = this.naviLoccation.height + "px";
    },
    storeNavi(event) {
      const id = event.target.parentNode.getAttribute("navi-id");
      this.naviLoccation = document
        .querySelector(`li[navi-id="${id}"]`)
        .getBoundingClientRect();
      if (id === "1") {
        this.$router.push({ name: "home" });
      }
      if (id === "5") {
        this.$router.push({ name: "mybook" });
      }
      console.log(id);
      this.$store.commit("changeNaviLoc", id);
    },
  },
};
</script>