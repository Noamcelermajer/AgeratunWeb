<template>
    <Chatbot/>
</template>


<script>
import Chatbot from '../components/Chatbot.vue';
export default {
  components: {
    Chatbot,
  },
  data() {
    return {
      isSticky: false,
    };
  },
  methods: {
},
};
</script>

<style lang="scss" scoped>
/* Add the fixed position to the header */
.absolute {
  position: fixed;
  width: 100%; // Ensure it spans the full width
}

/* Add padding to the top of the main content to prevent overlap */
.spacer-header{
  height: 80px; // You may need to adjust this value based on the height of your header
}
</style>
