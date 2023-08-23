<template>
  <div class="relative w-full h-[50px] py-4 bg-transparent contact-input">
    <select class="absolute left-0 bg-transparent border-0 text-[#515151] w-[60px] appearance-none" v-model="selectedCode">
      <option v-for="code in countryCodes" :key="code" :value="code">{{ code }}</option>
    </select>
    <input
      type="text"
      class="pl-[80px] text-[15px] w-full h-full text-[#515151] border-0 rounded-[4px] bg-transparent focus:outline-none focus:border-0 focus:border-black focus:shadow-none"
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
