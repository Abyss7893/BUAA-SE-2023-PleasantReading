<template>
  <el-card class="box-card" :body-style="{ padding: '0px' }">
    <!-- <template #header> -->
    <div class="card-header">
      <h1 class="title" style="margin: 5% 5% 5% 0">
        <span style="color: rgb(58, 21, 21)">{{ title }} </span>
        <span style="color: rgb(187, 52, 52)"> No.1</span>
      </h1>
      <div class="first-top">
        <img :src="booklist[0].cover" class="image" />
        <div class="first">
          <h2 class="book-name">{{ booklist[0].name }} aaaaaaaaaaaaaaaaaaa</h2>
          <p class="author">{{ booklist[0].author }}aaaaaaaaa著</p>
          <el-space size="10%">
            <el-tag class="mx-4" effect="plain" type="danger">{{
              booklist[0].state[0]
            }}</el-tag>
            <el-tag class="mx-4" effect="plain" type="danger">{{
              booklist[0].state[1]
            }}</el-tag>
            <el-tag class="mx-4" effect="plain" type="danger">{{
              booklist[0].state[2]
            }}</el-tag>
          </el-space>
        </div>
      </div>
    </div>
    <div class="text item">
      <span style="white-space: pre"> {{ " " }}</span>
    </div>

    <div class="other-books">
      <!-- </template> -->
      <div
        v-for="(book, index) in booklist.slice(1)"
        :key="book"
        class="text item"
      >
        No.{{ index + 2 }}:{{ book.name }}
      </div>
    </div>
  </el-card>
</template>
    
<script>
export default {
  props: {
    booklist: {
      type: Array,
      default: () => [],
    },
    title: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      rowsize: 10,
    };
  },
};
</script>

    
<style scoped>
.other-books {
  margin-top: -20px;
  padding-top: 10px;
  border-top: solid rgba(255, 86, 86, 0.242);
  display: block;
}
.author {
  font-family: kaiti;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 50%;
  padding-bottom: 2%;
}
.card-header {
  margin-left: 20px;
  float: left;
  justify-content: space-between;
  align-items: center;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100%;
}
.title {
  font-size: 20px;
  padding: 0px;
}
.book-name {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 50%;
  padding-bottom: 2%;
}
.first-top {
  display: flex;
}
.first {
  float: left;
  padding-left: 20px;
}
.text {
  font-size: 14px;
  padding-left: 20px;
}

.item {
  margin-bottom: 10px;
}
.image {
  width: 18%;
  min-width: 18%;
  border-radius: 4% 4% 4% 4%;
}
.el-card__body {
  margin: 10px;
}
.box-card {
  /* width: 480px; */
  width: 100%;
  max-width: 100%;
  min-width: 100%;
  background-color: rgba(157, 50, 50, 0.034);
}
</style>