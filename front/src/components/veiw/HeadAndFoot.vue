<template>
  <div>
    <WebHead />

    <slot></slot>
    <FootComponents />
  </div>
</template>
<script>
import WebHead from "./head/WebHead.vue";
import FootComponents from "./foot/WebFoot.vue";
// import { ElAffix } from "element-plus";
export default {
  name: "HeadAndFoot",
  components: {
    WebHead,
    FootComponents,

    // ElAffix,
  },
};
</script>