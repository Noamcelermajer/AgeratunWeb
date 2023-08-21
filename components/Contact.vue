<template>
    <div class="container-fluid section-padding">
      <div class="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center">
        <span class="text-sm leading-[1.714] block uppercase text-primary">Leave Contact Information</span>
        <h2 class="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase text-black"><a href="tel:+000000000000">+000000000000</a></h2>
      </div>
      <div class="w-full sm:w-2/3 mx-auto">
        <form id="contact-form" @submit.prevent="submitForm" class="grid gap-x-10 grid-cols-2">
          <div class="single-fild col-span-2 sm:col-span-1 mb-5">
            <input type="text" placeholder="Full Name" v-model="form.fullName" class="contact-input">
          </div>
          <div class="single-fild col-span-2 sm:col-span-1 mb-5">
            <input type="email" placeholder="Email" v-model="form.email" class="contact-input">
          </div>
          <PhoneInput v-model="phoneNumber" />
          <div class="single-fild col-span-2">
            <button type="submit" class="btn btn-md btn-outline-black btn-hover-primary max-w-[180px] sm:max-w-[200px] w-full">Send Message</button>
            <p class="form-messege"></p>
          </div>
        </form>
      </div>
      <div class="section-padding pb-0"></div>
    </div>
  </template>
  
  <script>
  import PhoneInput from './PhoneInput.vue';
  export default {
    data() {
      return {
        form: {
          fullName: '',
          email: '',
          countryCode: '+1',
          phoneNumber: ''
        }
      };
    },
    methods: {
      submitForm() {
        // Submit the form
        console.log(this.form);
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
  