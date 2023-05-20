<template>
  <WebHead />
  <ReaderBody />
  <WebFoot />
</template>
<script>
import WebHead from '../veiw/head/WebHead.vue';
import WebFoot from '../veiw/foot/WebFoot.vue';
import ReaderBody from '../veiw/body/ReaderBody.vue';

export default {
  name: "ReaderComponent",
  components: {
    WebHead,
    WebFoot,
    ReaderBody,

  },

}
</script>