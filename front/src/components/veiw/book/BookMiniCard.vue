<template>
  <!-- <transition name="el-fade-in-linear"> -->
  <div class="book-item">
    <router-link :to="'/book/' + book.id">
      <div class="book-img-box">
        <img :src="book.cover" alt="Book Cover" />
        <!-- <span>{{ book.cover }}</span> -->
      </div>
    </router-link>

    <div class="book-mid-info">
      <router-link :to="'/book/' + book.id">
        <h3 class="title">{{ book.title }}</h3></router-link
      >

      <div class="author">
        <p class="name">{{ book.author }}</p>

        <el-divider direction="vertical"></el-divider>
        <p class="category">{{ book.category }}</p>
        <!-- <em>|</em> -->
        <el-divider direction="vertical"></el-divider>
        <span>连载</span>
      </div>

      <p class="intro">{{ book.summary }}</p>

      <!-- <div class="book-rating"> -->
      <div class="book-rating-text">评分:{{ book.rating }}</div>

      <el-rate
        v-model="rating"
        style="--el-rate-fill-color: #ff7d7dc9"
        :disabled="true"
      ></el-rate>

      <p class="size">字数:{{ book.sizeString }}</p>
    </div>
  </div>
  <!-- </transition> -->
</template>

<script>
// import { getBookDetiles } from '@/api/api';
export default {
  props: {
    book: Object,
  },
  data() {
    return { rating: this.book.rating };
  },

};
</script>

<style scpoed>
.book-item {
  width: 100%;
  height: 100%;
  /* flex-basis: calc(50% - 10px);  */
  display: flex;

  margin: 0px;
  /* background: url("../../assets/imgs/shuqian.jpg") ; */
  background-size: 100% 100%;
  /* background-attachment: fixed; */
  /* background-color: aliceblue; */

  /* background-color: #3627076b; */
  padding: 10px;
  border-radius: 4px;
  text-align: left;
}

.book-info {
  margin-left: 10px;
  /* text-overflow: ellipsis; */
  text-align: left;
}

.book-rating-text {
  font-size: 12px;
  margin-top: auto;
  font-weight: bold;
}
.book-rating {
  display: flex;
}
.book-img-box {
  display: block;

  height: 186px;
  margin-right: 16px;
  position: relative;
  /* max-width: 102px;
  min-width: 102px; */
  /* box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); */
  z-index: 3;
}
.book-img-box img {
  width: 100%;
  height: 100%;
  overflow: hidden;

  transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s;
  border-radius: 4%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)
  /* z-index: 10; */
}
.book-img-box img:hover {
  transform: scale(1.1);
}

.book-mid-info {
  max-width: 280px;
  min-width: 280px;
  margin-top: 5px;

  /* float: left;
  overflow: hidden;
  text-overflow: nowrap; */
  /* white-space: nowrap; */

  /* text-overflow: ellipsis; */
}
.intro {
  color: #743e13a6;
  font-size: 14px;
  max-height: 48px;
  min-height: 48px;
  line-height: 24px;
  margin-bottom: 8px;
  width: 100%;
  font-family: kaiti;

  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; /* 这里是超出几行省略 */
  overflow: hidden;

  /* overflow: hidden; */
}

/* .el-row {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
  max-height: 210px;
  min-height: 210px;
}
.el-col {
  max-height: 210px;
  min-height: 210px;
} */
.title {
  color: #231e1e;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding: 0px;
  /* text-overflow: ellipsis; */
  /* white-space: normal; */
  /* background: #030958; */
}
.author {
  height: 22px;
  margin-bottom: 6px;
  display: flex;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  /* border-top:solid #c6b7b758; */
  /* overflow: hidden; */
}
.name {
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}
.category {
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}
.size {
  font-size: small;
  color: #666;
}
</style>