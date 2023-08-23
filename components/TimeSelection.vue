// TimeSelection.vue

<template>
  <div>
    <h2 class="text-lg mb-4">Select a time slot for {{ selectedDate }}</h2>
    <div class="flex flex-wrap">
      <div
        v-for="time in availableTimes"
        :key="time"
        @click="selectTime(time)"
        class="cursor-pointer p-4 border border-gray-300 w-1/4 hover:bg-gray-100"
      >
        {{ time }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['selectedDate'],
  data() {
    return {
      availableTimes: ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
      selectedTime: null,
    };
  },
  mounted() {
    // Retrieve the selected date from the query parameters
    this.selectedDate = this.$route.query.date;
  },
  methods: {
    selectTime(time) {
      this.selectedTime = time;
      this.$router.push({
        path: '/schedule/confirmation',
        query: { date: this.selectedDate, time: this.selectedTime },
      });
    },
  },
};

</script>
