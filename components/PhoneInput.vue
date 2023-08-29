<template>
  <div class="relative w-full h-12 py-2 bg-transparent contact-input">
    <select class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-transparent border-0 text-gray-600 w-16 appearance-none leading-5 text-base" v-model="selectedCode">
      <option v-for="code in countryCodes" :key="code" :value="code">{{ code }}</option>
    </select>
    <input
      @input="validateNumber"
      type="text"
      class="pl-20 text-base w-full h-full text-gray-600 border-0 rounded bg-transparent focus:outline-none focus:border-0 focus:border-black focus:shadow-none"
      placeholder="Phone"
      v-model="phoneNumber"
    />
  </div>
</template>



<script>
export default {
data() {
  return {
    selectedCode: '+1',
    countryCodes: ['+1', '+44', '+33', '+972'], // Add more country codes here
    phoneNumber: ''
  };
},
methods: {
    validateNumber(event) {
      this.phoneNumber = this.phoneNumber.replace(/[^0-9]/g, '');
    }
  }
};
</script>
<style scoped>
.contact-input {
    font-size: 15px;
    color: #515151;
    border-top: 0;
    border-left: 0;
    border-right: 0;
    border-bottom: 1px solid #cfcfd4;
    border-radius: 4px;
    background-color: transparent;
    outline: 0;
    transition: all 0.5s;
}
.contact-input:focus-within {
    border-color: black;
    box-shadow: none;
}
.adjusted-select {
  margin-top: 10px; /* Adjust this value to fit your needs */
}
select {
    background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4 5"><path fill="none" stroke="#515151" d="M2 0L0 4h4z"/></svg>');
    background-repeat: no-repeat;
    background-position: right 5px center;
    background-size: 12px;
    padding-top: 0; /* Adjust padding if needed */
    margin-top: 2px; /* Adjust margin to align select with border */
    line-height: normal; /* Adjust line height to fit with other input elements */
}
</style>
