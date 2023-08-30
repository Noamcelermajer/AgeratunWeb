<template>
  <div class="single-fild col-span-2 sm:col-span-1 mb-5 flex items-center h-12 py-2 bg-transparent">
    <div class="relative w-1/4 h-[50px]">
      <input
      @input="autocomplete"
      type="text"
      class="text-base w-full h-full text-gray-600 border-b border-gray-300 focus:border-black rounded bg-transparent focus:outline-none"
      placeholder="Country Code"
      v-model="inputValue"
      name="countryCode"
    />
    <div v-if="showPopup" class="absolute left-0 mt-2 w-full rounded bg-red-500 text-white p-2">
      Invalid Phone Number
    </div>
      <ul v-if="showSuggestions" class="absolute top-full left-0 w-full bg-white border border-gray-300 rounded">
        <li v-for="code in filteredCodes" @click="selectCode(code)" class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
          {{ code }}
        </li>
      </ul>
    </div>
    <div class="flex-initial ml-2 w-3/4 h-[50px]">
      <input
        @input="validateNumber"
        type="text"
        class="text-base w-full h-full text-gray-600 border-b border-gray-300 focus:border-black rounded bg-transparent focus:outline-none"
        placeholder="Phone"
        v-model="phoneNumber"
        name="phoneNumber"
      />
    </div>
  </div>
</template>

<script>
import codes from '@/data/codes.json';

export default {
  data() {
    return {
      showPopup: false,
      inputValue: '',
      countryCodes: codes.map(item => item['dial_code']),
      filteredCodes: [],
      showSuggestions: false,
      phoneNumber: ''
    };
  },
  methods: {
    autocomplete() {
      this.filteredCodes = this.countryCodes.filter(code =>
        code.includes(this.inputValue)
      );
      this.showSuggestions = true;
    },
    selectCode(code) {
      this.inputValue = code;
      this.showSuggestions = false;
    },
    validateNumber() {
    this.phoneNumber = this.phoneNumber.replace(/[^0-9]/g, '');
    if (!this.phoneNumber || this.phoneNumber.length < 10) {
      this.showPopup = true;
    } else {
      this.showPopup = false;
    }
  }},
  watch: {
    inputValue(newVal) {
      this.inputValue = newVal.replace(/[^+0-9]/g, '');
    }
  }
};
</script>

<style scoped>
.contact-input:focus {
  border-bottom: 1px solid black;
}
</style>
