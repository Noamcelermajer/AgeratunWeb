<template>
  <div class="container-fluid section-padding">
    <div class="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center">
      <h2 class="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal  text-primary">
        <a>Leave Contact Information</a>
      </h2>
    </div>
    <div class="w-full sm:w-2/3 mx-auto">
      <form id="contact-form" class="space-y-5" @submit.prevent="submitForm">
        <!-- First and Last Name Fields -->
        <div class="flex space-x-2 mb-5">
          <input type="text" :title="errors.firstName" placeholder="First Name" v-model="form.firstName" name="firstName"
            class="text-base flex-1 text-gray-600 border-b border-gray-300 focus:border-black rounded bg-transparent focus:outline-none" />
          <input type="text" :title="errors.lastName" placeholder="Last Name" v-model="form.lastName" name="lastName"
            class="text-base flex-1 text-gray-600 border-b border-gray-300 focus:border-black rounded bg-transparent focus:outline-none" />
        </div>
        <!-- Phone Input Field -->
        <div class="flex space-x-2 mb-5">
          <input @input="autocomplete" type="text" 
            class="text-base flex-1 text-gray-600 contact-input rounded bg-transparent focus:outline-none"
            placeholder="Country Code" v-model="inputValue" name="countryCode" />
          <input @input="validateNumber" type="text"
            class="text-base flex-1 text-gray-600 contact-input rounded bg-transparent focus:outline-none"
            placeholder="Phone" v-model="phoneNumber" name="phoneNumber" />
        </div>
        <!-- Email Field -->
        <div class="mb-5">
          <input type="email" :title="errors.email" placeholder="Email" v-model="form.email" name="email"
            class="contact-input w-full">
        </div>
        <!-- Submit Button -->
        <div class="flex justify-center mt-5 mb-5">
          <ButtonDefault :btnClass="btnClass" :btnText="btnText" @click="submitForm" :isSubmit=true :disabled="!isValid">
          </ButtonDefault>
        </div>
      </form>
    </div>
  </div>
</template>



<script>
import ButtonDefault from '@/components/button/ButtonDefault.vue'; // Correct path to the button component
import codes from '@/data/codes.json'; // Assuming you have this file

export default {
  components: {
    ButtonDefault
  },
  data() {
    return {
      errors: {
        fullName: '',
        email: '',
        phoneNumber: ''
      },
      form: {
        fullName: '',
        email: '',
        countryCode: '',  // Added this line
        phoneNumber: '',
      },
      isValid: false,
      btnClass: 'text-center btn btn-md btn-outline-black btn-hover-primary max-w-[180px] sm:max-w-[200px] w-full',
      btnText: 'Send Message',
      showPopup: false,
      inputValue: '',
      countryCodes: codes.map(item => item['dial_code']),
      filteredCodes: [],
      showSuggestions: false,
      phoneNumber: '',
    };
  },
  methods: {
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
  },
    autocomplete() {
      this.filteredCodes = this.countryCodes.filter(code =>
        code.includes(this.inputValue)
      );
      this.showSuggestions = true;
    },
    handlePhoneData() {
      this.form.countryCode = this.inputValue;
      this.form.phoneNumber = this.phoneNumber;
    },
    mounted() { window.history.replaceState(null, null, ' '); },
    validateForm() {
      this.isValid = true;

      if (!this.form.fullName) {
        this.errors.fullName = 'Full Name is required';
        this.isValid = false;
      } else {
        this.errors.fullName = '';
      }

      if (!this.form.email || !/\S+@\S+\.\S+/.test(this.form.email)) {
        this.errors.email = 'Valid Email is required';
        this.isValid = false;
      } else {
        this.errors.email = '';
      }

      if (!this.form.phoneNumber) {
        this.errors.phoneNumber = 'Phone Number is required';
        this.isValid = false;
      } else {
        this.errors.phoneNumber = '';
      }
    },
    submitForm() {
      this.validateForm();

      if (!this.isValid) return;
      // Prepare the form data
      const formData = new FormData();
      formData.append('fullName', this.form.fullName);
      formData.append('email', this.form.email);
      formData.append('countryCode', this.form.countryCode); // Added this line
      formData.append('phoneNumber', this.form.phoneNumber);

      // Use Fetch API to send the form data
      fetch('https://getform.io/f/fa39ccd7-2ac9-490d-910e-4202b2f8e46b', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          console.log('Success:', data);
          window.location.href = "https://getform.io/thank-you"; // Redirect to the thank-you page
        })
        .catch((error) => {
          console.error('Error:', error);
        });

      // Emit an event to signal the parent component
      this.$emit('contactFinished');
    }
  },
  watch: {
    inputValue(newVal) {
      this.inputValue = newVal.replace(/[^+0-9]/g, '');
    },
    phoneNumber(newVal) {
      this.handlePhoneData();
    },
    form: {
      handler: 'validateForm',
      deep: true
    }
  }
};
</script>

<style>
.contact-input {
  font-size: 15px;
  position: relative;
  display: block;
  width: 100%;
  height: 50px;
  padding: 4px 0;
  transition: all 0.5s;
  color: #515151;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  border-bottom: 1px solid #cfcfd4;
  border-radius: 4px;
  background-color: transparent;
  outline: 0;
}

.contact-input:focus {
  border-color: black;
  box-shadow: none;
}
</style>
