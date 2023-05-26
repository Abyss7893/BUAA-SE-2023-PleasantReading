<template>
  <el-card :body-style="{ padding: '0px' }" shadow="hover" @click="gotoRead">
    <img :src="cover" class="image" />
    <div class="title">
      <el-tooltip
        class="box-item"
        effect="dark"
        :content="name"
        placement="bottom"
      >
        <span>{{ name }}</span>
      </el-tooltip>
    </div>
  </el-card>
</template>
  
  <script>
// import { nextTick } from 'vue';
export default {
  props: {
    cover: String,
    name: String,
    bookid: String,
  },
  methods: {
    gotoRead() {
      console.log("gotoRead" + this.bookid);
      this.$router.push({
        path: "/book/" + this.bookid ,
      });
    },
  },
};
</script>
  
<style scoped>
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
  min-height: 170px;
  max-height: 170px;
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