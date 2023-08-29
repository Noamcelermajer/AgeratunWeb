<template>
  <div class="container-fluid section-padding">
    <div class="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center">
      <h2 class="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal  text-primary">
        <a >Leave Contact Information</a>
      </h2>
    </div>
    <div class="w-full sm:w-2/3 mx-auto">
      <form class="grid gap-x-10 grid-cols-2" id="contact-form" action="https://getform.io/f/fa39ccd7-2ac9-490d-910e-4202b2f8e46b" method="POST">
        <div class="single-fild col-span-2 sm:col-span-1 mb-5">
          <input type="text" placeholder="Full Name" v-model="form.fullName" name="fullName" class="contact-input">
        </div>
        <div class="single-fild col-span-2 sm:col-span-1 mb-5">
          <input type="email" placeholder="Email" v-model="form.email" name="email" class="contact-input">
        </div>
        <PhoneInput v-model="form.phoneNumber" name="phoneNumber"/>
        <div class="single-fild col-span-2 flex justify-center items-start mt-5 mb-5">
          <ButtonDefault :btnClass="btnClass" :btnText="btnText" @click="submitForm" :isSubmit=true></ButtonDefault>
          <p class="form-messege"></p>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import PhoneInput from './PhoneInput.vue';
import ButtonDefault from '@/components/button/ButtonDefault.vue'; // Correct path to the button component

export default {
  components: {
    PhoneInput,
    ButtonDefault
  },
  data() {
    return {
      form: {
        fullName: '',
        email: '',
        countryCode: '+1',
        phoneNumber: '',
      },
      btnClass: 'text-center btn btn-md btn-outline-black btn-hover-primary max-w-[180px] sm:max-w-[200px] w-full',
      btnText: 'Send Message'
    };
  },
  methods: {
    mounted(){  window.history.replaceState(null, null, ' ');},
    submitForm() {
    // Prepare the form data
    const formData = new FormData();
    formData.append('fullName', this.form.fullName);
    formData.append('email', this.form.email);
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
