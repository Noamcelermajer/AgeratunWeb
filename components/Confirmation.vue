// Confirmation.vue

<template>
  <div>
    <h2 class="text-lg mb-4">Confirm Your Meeting</h2>
    <div>
      Date: {{ selectedDate }}
      <br />
      Time: {{ selectedTime }}
    </div>
    <button @click="confirmMeeting" class="bg-blue-500 text-white p-2 mt-4 hover:bg-blue-600">
      Confirm Meeting
    </button>
  </div>
</template>

<script>

import axios from 'axios';
export default {

  props: ['selectedDate', 'selectedTime'],
  methods: {
    confirmMeeting() {
    axios.post('/schedule-meeting', { date: this.selectedDate, time: this.selectedTime })
      .then(response => {
        alert('Meeting scheduled successfully!');
      })
      .catch(error => {
        console.error('An error occurred while scheduling the meeting:', error);
        alert('Failed to schedule the meeting. Please try again.');
      });
    },
  },
};
</script>
