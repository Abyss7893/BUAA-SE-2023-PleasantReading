<template>
  <div class="container">
    <!-- 第一个卡片 -->
    <div class="card">
      <div class="content">
        <!-- <h2>01</h2> -->
        <h3>Card One ddd dd ddd</h3>
        <p>Lorem ipsum dolor sit amet amet amet</p>
        <!-- <a href="#">Read More</a> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props() {
    return {
      title: "Card One",
    };
  },
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
  position: relative;
  background-image: url("../../../../assets/girl.png");
  background-size: 100% 100%;
  width: 280px;
  height: 200px;
  margin: 0px;
  box-shadow: 20px 20px 50px rgba(0, 0, 0, 0.5);
  border-radius: 15px;

  /* overflow: hidden; */
  display: flex;
  justify-content: center;
  align-items: center;
  /* border-top: 1px solid rgba(255, 255, 255, 0.5); */
  border-left: 1px solid rgba(255, 255, 255, 0.5);
  /* overflow: hidden; */
  overflow: hidden;
}
.container .card .content {
  /* background-image: "../../../../assets/girl.png"; */
  /* padding: 20px; */
  text-align: center;
  height: inherit;
  transform: translateY(100%);
  opacity: 0;
  border-radius: inherit;
  transition: 0.5s;

  /* background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  transform: translateY(0px);
  opacity: 1; */
}
.container .card:hover .content {
  background: rgba(129, 85, 85, 0.548);
  /* backdrop-filter: blur(2px); */
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
  margin-left: 10px;
  margin-right: 10px;
  overflow: hidden;
  top: -60px;
  right: 1px;
  color: rgba(255, 255, 255, 0.05);
  /* font-size: 1.8em; */
  color: #fff;
  z-index: 1;
}
.container .card .content p {
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

