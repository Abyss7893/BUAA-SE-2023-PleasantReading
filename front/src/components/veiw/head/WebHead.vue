<!-- 网页头部 -->
<template>
  <Head_Top />
  <ElAffix>
    <Head_Nav />
  </ElAffix>
</template>
<script>
import Head_Top from "./HeadTop.vue";
import Head_Nav from "./HeadNav.vue";
import "css/head/head.css";
export default {
  name: "Web_Head",
  components: {
    Head_Top,
    Head_Nav,
  },
};
</script>