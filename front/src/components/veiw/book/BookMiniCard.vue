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
        <h3 class="title">{{ book.title }}</h3>
      </router-link>

      <div class="author">
        <a class="name" :href="'/author/' + book.author">{{ book.author }}著</a>
      </div>
      <el-space size="10%">
        <el-tag class="mx-4" effect="plain" type="danger">
          <p class="category">{{ book.category }}</p>
        </el-tag>
        <el-tag class="mx-4" effect="plain" type="danger">{{
          book.status
        }}</el-tag>
        <el-tag class="mx-4" effect="plain" type="danger">{{
          book.vip
        }}</el-tag>
        <el-tag class="mx-4" effect="plain" type="danger">{{
          book.simpleSizes
        }}</el-tag>
      </el-space>
      <!-- <div class="author">
        <el-divider direction="vertical"></el-divider>
       
        <el-divider direction="vertical"></el-divider>
        <span>{{ book.status }}</span>
      </div> -->
      <!-- <div class="book-state">
        <span class="state hidden-sm">{{ book.status }}</span>
        <span class="state hidden-sm">{{ book.vip }}</span>
        <span class="state hidden-sm">{{ book.simpleSizes }}</span>
        <span class="state hidden-sm">{{ book.category }}</span>
      </div> -->

      <p class="intro">{{ book.summary }}</p>

      <!-- <div class="book-rating"> -->
      <div class="otherintro" style="display: flex">
        <div class="leftside">
          <div class="book-rating-text">评分:{{ book.rating }}</div>

          <el-rate
            v-model="rating"
            style="--el-rate-fill-color: #ff7d7dc9"
            :disabled="true"
          ></el-rate>

          <p class="size">字数:{{ book.size }}</p>
        </div>
        <!-- <div class="rightside">
          <el-tag class="ml-2" type="danger">Tag 5</el-tag>
        </div> -->
      </div>
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
  // data() {
  //   return { rating: this.book.rating };
  // },
  computed: {
    rating() {
      return this.book.rating;
    },
  },
};
</script>

<style scpoed>
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
  border-radius: 20px;
  text-align: left;
  transition: 0.2s;
  /* background-color: rgba(2, 1, 4, 0); */
}

.book-item:hover {
  border: solid rgba(255, 0, 0, 0.21) 1px;
  background-color: rgba(216, 138, 145, 0.068);
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
  margin-top: 15px;
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
  max-width: 131px;
  min-height: 186px;
  overflow: hidden;
  max-height: 186px;
  transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s;
  border-radius: 7%;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2), 0 3px 5px 0 rgba(0, 0, 0, 0.19);

  /* z-index: 10; */
}

.book-img-box img:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
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
  margin-bottom: 6px;
  margin-top: 6px;
  width: 100%;
  font-family: kaiti;

  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  /* 这里是超出几行省略 */
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
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}

.name:hover {
  color: #f56c6c;
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