<template>
  <HeadAndFoot>
    <SearchBook />
  </HeadAndFoot>
</template>
<script>
import SearchBook from '../veiw/body/search/SearchBook.vue';
import HeadAndFoot from '../veiw/HeadAndFoot.vue';
export default {
  name: "seachPage",
  data() {
    return {
      bookIds: null,
    }
  },
  components: {
    SearchBook,
    HeadAndFoot,
  },
}
</script>