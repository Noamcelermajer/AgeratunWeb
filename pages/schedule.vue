<template>
  <div>
    <!-- Header Component -->
    <div class="absolute top-0 left-0 right-0 z-[999]" :class="{'is-sticky': isSticky}">
      <div class="container-fluid mx-auto">
        <div class="flex justify-between items-center">
          <div class="flex items-center" >
            <Logo v-if="!isSticky" class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/"/>
            <LogoDark v-else class="relative z-50 sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/"/>
          </div>
          <div class="flex items-center">
            <ButtonDefault 
            :btnLink="'#contact-section'"
            :btnClass="'btn-sm btn btn-hover-primary btn-outline-light'"
            :btnText="'Schedule a visit'"
            :btnClassParent="'flex'"
            class="hidden sm:inline-flex"
            @click="askForAppointment" 
          />

                  </div>
              </div>
          </div>
      </div>
      <div class="spacer-header"></div>


    <!-- Contact Form (Schedule Section) -->
    <Contact v-if="!showScheduleAppointment" @contactFinished="askForAppointment" />

    <!-- Schedule Appointment Component -->
    <ScheduleAppointment v-if="showScheduleAppointment" />

    <!-- Footer Component -->
    <FooterSectionTwo />
  </div>
</template>


<script>
import MainHeader from '@/components/header/MainHeader.vue';
import FooterSectionTwo from '@/components/FooterSectionTwo.vue';
import Contact from '@/components/Contact.vue';
import ScheduleAppointment from '@/components/Schedule-Appointment.vue'; // Updated import path

export default {
  components: {
    MainHeader,
    FooterSectionTwo,
    Contact,
    ScheduleAppointment,
  },
  data() {
    return {
      showScheduleAppointment: false,
      isSticky: false,
    };
  },
  methods: {
  askForAppointment() {
    if (confirm('Would you like to appoint a meeting?')) {
      this.showScheduleAppointment = true;
    }
  },
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
