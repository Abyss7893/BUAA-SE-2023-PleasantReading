<template>
  <div>
    <!-- 页面内容 -->
    <footer class="footer">
      <AboutC />
      <ContactUs />
      <HelpC />
    </footer>
  </div>
</template>


<script>
import ContactUs from "./foots/ContactUs.vue";
import AboutC from "./foots/AboutC.vue";
import HelpC from "./foots/HelpC.vue";
import "@/assets/css/foot/foot.css";
export default {
  components: {
    AboutC,
    ContactUs,
    HelpC
  },
};
</script>

<style></style>