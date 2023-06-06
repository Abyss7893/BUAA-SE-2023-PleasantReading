<template>
  <HeadTop :holdplace="true" />
  <ReaderBody />
  <WebFoot />
</template>
<script>
import HeadTop from "../veiw/head/HeadTop.vue";
import WebFoot from "../veiw/foot/WebFoot.vue";
import ReaderBody from "../veiw/body/ReaderBody.vue";
import { stopp } from "@/api/sakura";
export default {
  name: "ReaderComponent",
  components: {
    HeadTop,
    WebFoot,
    ReaderBody,
  },
  created() {
    stopp();
  },
};
</script>