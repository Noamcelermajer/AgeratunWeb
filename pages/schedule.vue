<template>
  <div>
    <!-- Header Component -->
    <MainHeader textClass="your-text-class-if-needed" />

    <!-- Contact Form (Schedule Section) -->
    <Contact />

    <!-- Footer Component -->
    <FooterSectionTwo />
  </div>
</template>

<script>
import MainHeader from '@/components/header/MainHeader.vue';
import FooterSectionTwo from '@/components/FooterSectionTwo.vue';
import Contact from '@/components/Contact.vue';

export default {
  components: {
    MainHeader,
    FooterSectionTwo,
    Contact
  }
}
</script>

<style lang="scss" scoped>
  /* Add any specific styles for the Schedule page here */
</style>
