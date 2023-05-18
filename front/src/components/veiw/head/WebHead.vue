<!-- 网页头部 -->
<template>
  <div class="head">
    <ElAffix>
      <Head_Top />
      <Head_Nav />
    </ElAffix>
  </div>
</template>
<script>
import Head_Top from './HeadTop.vue';
import Head_Nav from './HeadNav.vue';
import { ElAffix } from 'element-plus';
import "css/head/head.css"
export default {
  name: 'Web_Head',
  components: {
    Head_Top,
    Head_Nav,
    ElAffix,
  }
}
</script>