<template>
  <div class="basic-bcg">
    <ReaderMenu ref="child1" />
    <!-- 包裹在容器中，限定宽高，并传入文本内容 -->
    <ReaderComponent />

  </div>
</template>

<script>
import ReaderComponent from './reader/ReaderComponent.vue';
import ReaderMenu from './reader/ReaderMenu.vue';

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
  computed: {

  },
  components: {
    ReaderComponent,
    ReaderMenu,

  },
}
</script>