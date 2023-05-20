<template>
  <el-card :body-style="{ padding: '0px' }">
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
  z-index: 1;
}

.image {
  width: 100%;
  display: block;
  /* max-height: 207px; */
  overflow: hidden;

  transition-property: all;
  transition-duration: 0.5s;
  transition-timing-function: ease;
  transition-delay: 0s;
  z-index: 10;
}

.image:hover {
  transform: scale(1.2);
}
</style>