<template>
  <HeadAndFoot>
    <AuthorBody />
  </HeadAndFoot>
</template>

<script>
import AuthorBody from '../veiw/body/author/AuthorBody.vue';
import HeadAndFoot from '../veiw/HeadAndFoot.vue';
export default {
  name: 'AuthorPage',
  components: { HeadAndFoot, AuthorBody },
};
</script>
