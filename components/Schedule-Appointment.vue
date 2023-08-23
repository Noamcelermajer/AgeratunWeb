<template>
  <div class="rounded-lg p-6 bg-light space-y-4 max-w-xl mx-auto">
    <!-- Dates Selection (on top) -->
    <div class="flex overflow-x-scroll space-x-2 mb-4">
      <div 
        v-for="day in next7Days" 
        @click="selectDate(day)" 
        :class="{'opacity-50 cursor-not-allowed': unavailableDates.includes(formatDate(day)), 'cursor-pointer p-2 border border-gray-300 hover:bg-gray-100 rounded-md': true}">
        {{ displayDate(day) }}
      </div>
    </div>

    <!-- Step 1: Display Selected Date and Select Time -->
    <div v-if="step === 2" class="animate__fadeUp2">
      <h2 class="text-xl font-bold text-dark mb-4">Select a Time for {{ formatDate(selectedDate) }}</h2>
      <div v-for="time in availableTimes" @click="selectTime(time)" class="cursor-pointer p-4 border-1 border-bordercolor w-1/4 hover:bg-gray-100 mb-2 inline-block rounded">
        {{ time }}
      </div>
    </div>

    <!-- Step 2: Confirm Meeting -->
    <div v-if="step === 3" class="animate__fadeUp3">
      <h2 class="text-xl font-bold text-dark mb-4">Confirm Your Meeting</h2>
      <div class="text-themedark">
        Date: {{ formatDate(selectedDate) }}
        <br />
        Time: {{ selectedTime }}
      </div>
      <button @click="confirmMeeting" class="bg-primary text-white p-2 mt-4 hover:bg-dark rounded">Confirm Meeting</button>
    </div>
  </div>
</template>


  
  
  <script>
  import axios from 'axios';
  import { addDays, format } from 'date-fns';
  
  export default {
    data() {
      return {
        step: 1,
        next7Days: Array.from({ length: 7 }, (_, i) => addDays(new Date(), i)),
        unavailableDates: [], // Store the unavailable dates here
        selectedDate: null,
        availableTimes: this.generateTimeSlots(),
        selectedTime: null,
        unavailableTimes: [],
      };
    },
    methods: {
      // Generate 15-minute time slots from 9:00 to 18:00
      generateTimeSlots() {
        const slots = [];
        for (let hour = 9; hour < 18; hour++) {
          for (let min = 0; min < 60; min += 15) {
            const time = `${hour.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}`;
            slots.push(time);
          }
        }
        return slots;
      },
      formatDate(date, pattern = 'yyyy-MM-dd') {
      return format(date, pattern);
      },
      displayDate(date) {
      const dayName = format(date, 'EEEE'); // Name of day
      return format(date, 'MM/dd') + ' - ' + dayName; // MM/DD - [Name of day]
      },
      fetchUnavailableDates() {
        axios.get(`http://localhost:5000/unavailable-times/`)
        .then(response => {
        this.unavailableDates = response.data; // Update unavailableDates with the response
        })
        .catch(error => {
        console.error('An error occurred while fetching unavailable times:', error);
        });
    },



    selectDate(date) {
      if (this.unavailableDates.includes(this.formatDate(date))) return;
      this.selectedDate = date;
      this.fetchUnavailableDates(date); // Fixed the function name
      this.step = 2;
    },

      selectTime(time) {
        this.selectedTime = time;
        this.step = 3;
      },
      confirmMeeting() {
        // Replace with actual backend URL and payload
        axios.post('http://localhost:5000/schedule-meeting', { date: this.formatDate(this.selectedDate), time: this.selectedTime })
          .then(response => {
            alert('Meeting scheduled successfully!');
          })
          .catch(error => {
            console.error('An error occurred while scheduling the meeting:', error);
            alert('Failed to schedule the meeting. Please try again.');
          });
      },
    },
    created() {
    this.fetchUnavailableDates();
    }
  };
  </script>
  
  <style>
  .schedule-appointment-padding {
    padding-top: 100px; 
  }
</style>