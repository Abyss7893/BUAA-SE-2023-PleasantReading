<template>
  <div class="container">
    <!-- 第一个卡片 -->
    <div
      class="card"
      :style="{
        backgroundImage: `url(${'http://154.8.183.51/media/' + book.img})`,
      }"
    >
      <div class="content">
        <!-- <router-link :to="'/book/' + book.bookID"> -->
        <h3
          @click="
            () => {
              this.$router.push({ path: '/book/' + book.bookID });
            }
          "
        >
          {{ book.name }}
        </h3>
        <!-- </router-link> -->
        <!-- <router-link :to="'/reader/' + book.bookID + '/' + book.chapter"> -->
        <p
          @click="
            () => {
              this.$router.push({
                path: '/reader/' + book.bookID + '/' + book.chapter,
              });
            }
          "
        >
          {{ book.title }}ddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        </p>
        <!-- </router-link> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
  // props: {
  //   book: {
  //     type: Object,
  //     required: true,
  //     default: () => {
  //       return {
  //         img: ".jpg",
  //         name: "book.name",
  //         title: "book.title",
  //         bookID: 1,
  //         chapter: 1,
  //       };
  //     },
  //   },
  // },
  data() {
    return {};
  },
  methods() {},
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com");

.container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 1200px;
  flex-wrap: wrap;
  z-index: 1;
}
.container .card {
  /* background-image: url("../../../../assets/girl.png"); */
  position: relative;

  background-size: 100% 100%;
  width: 280px;
  height: 200px;
  margin: 0px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
  border-radius: 15px;

  /* overflow: hidden; */
  display: flex;
  justify-content: center;
  /* align-items: center; */
  /* border-top: 1px solid rgba(255, 255, 255, 0.5); */
  border-left: 1px solid rgba(255, 255, 255, 0.5);
  /* overflow: hidden; */
  /* overflow: hidden; */
  overflow: scroll;
  transition: 0.5s;
  
}
::-webkit-scrollbar {
  width: 0;
  height: 0;
  background-color: transparent;
}
.container .card:hover {
  /* background-image: url("../../../../assets/girl.png"); */
  scale: 1.1;
}
.container .card .content {
  /* padding: 20px; */
  text-align: center;
  min-height: 400px;
  transform: translateY(100%);
  opacity: 0;
  border-radius: inherit;
  transition: 0.5s;
  width: inherit;

  /* background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  transform: translateY(0px);
  opacity: 1; */
  /* background: rgba(53, 57, 80, 0.548);
  transform: translateY(0px);
  opacity: 1; */
}
.container .card:hover .content {
  background: rgba(53, 57, 80, 0.548);
  transform: translateY(0px);
  opacity: 1;
}
.container .card .content h2 {
  position: absolute;
  top: -60px;
  right: 1px;
  font-size: 10em;
  color: rgba(255, 255, 255, 0.05);
  pointer-events: none;
}
.container .card .content h3 {
  cursor: pointer;
  margin-top: 30px;
  white-space: normal;
  /* max-height: 200px; */
  white-space: normal;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  /* 这里是超出几行省略 */
  margin-left: 3px;
  margin-right: 3px;
  overflow: hidden;
  /* top: -60px; */
  right: 1px;
  color: rgba(255, 255, 255, 0.05);
  /* font-size: 1.8em; */
  color: #fff;
  z-index: 1;
}
.container .card .content p {
  cursor: pointer;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  white-space: normal;
  /* max-height: 200px; */
  white-space: normal;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  font-size: 1em;
  color: #fff;
  font-weight: 300;
}
.container .card .content a {
  position: relative;
  display: inline-block;
  padding: 8px 20px;
  margin-top: 15px;
  background: #fff;
  color: #000;
  border-radius: 20px;
  text-decoration: none;
  font-weight: 500;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
</style>

