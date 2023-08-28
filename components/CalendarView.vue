<template>
  <div class="flex flex-wrap">
    <div
      v-for="day in nextSevenDays"
      :key="day.date"
      @click="selectDay(day)"
      class="cursor-pointer p-4 border border-gray-300 w-1/4 hover:bg-gray-100"
    >
      <div>{{ day.date | formatDate }}</div>
      <div class="text-sm text-gray-500">{{ day.dayOfWeek }}</div>
    </div>
  </div>
</template>

<script>
import { addDays, format } from 'date-fns';

export default {
  data() {
    return {
      nextSevenDays: this.getNextSevenDays(),
      selectedDay: null,
    };
  },
  methods: {
    fetchTimeSlots() {
      axios.get('http://localhost:5000/api/timeslots')
        .then(response => {
          this.availableTimeSlots = response.data;
          this.currentOptions = this.availableTimeSlots;  // Enable buttons for available timeslots
        });
    },
    getNextSevenDays() {
      const days = [];
      for (let i = 0; i < 7; i++) {
        const date = addDays(new Date(), i);
        days.push({
          date: date,
          dayOfWeek: format(date, 'EEEE'),
        });
      }
      return days;
    },
    selectDay(day) {
      this.selectedDay = day;
      this.$router.push({ path: '/schedule/time-selection', query: { date: day.date } });
    },
  },
  filters: {
    formatDate(date) {
      return format(date, 'MM/dd/yyyy');
    },
  },
};
</script>
