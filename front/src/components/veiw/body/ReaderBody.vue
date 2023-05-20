<template>
  <div class="basic-bcg">
    <ElAffix>
      <ReaderMenu />
    </ElAffix>
    <!-- 包裹在容器中，限定宽高，并传入文本内容 -->
    <ReaderComponent />

  </div>
</template>

<script>
import ReaderComponent from './reader/ReaderComponent.vue';
import ReaderMenu from './reader/ReaderMenu.vue';
import { ElAffix } from 'element-plus';
export default {
  name: "ReaderBody",
  data() {
    return {
      content: {
        chapters: [],
        text: "",
      },
    };
  },
  components: {
    ReaderComponent,
    ReaderMenu,
    ElAffix,
  },
}
</script>