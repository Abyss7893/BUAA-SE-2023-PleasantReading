<template>
  <el-card :body-style="{ padding: '0px' }" shadow="hover">
    <img :src="cover" class="image" />
    <div class="title">
      <span>{{ name }}</span>
    </div>
  </el-card>
</template>
  
  <script>
export default {
  props: {
    cover: String,
    name: String,
  },
};
</script>
  
<style>
.title {
  padding: 14px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.image {
  width: 100%;
  display: block;
  border-radius: 15px 15px 0 0;
  /* max-height: 207px; */
  overflow: hidden;

  /* transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s;
  z-index: 10; */
}

/* .image:hover {
  transform: scale(1.2);
} */
.el-card {
  transition: all 0.5s;
  border-radius: 15px;
  background-color: rgba(255, 0, 0, 0.1);
}
.el-card:hover {
  margin-top: -7px;
}
</style>