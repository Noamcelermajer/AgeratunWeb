<template>
    <div class="flex items-center flex-col">
  
      <ul class="w-full grid grid-cols-1 lg:grid-cols-2 gap-7 md:gap-9 container-fluid section-padding pt-0">
        <li class="relative group" v-for="(item, index) in categories" :key="index" :class="[index === active ? 'trigger-active' : '']" @click='activate(index)'>
          <div class="cursor-pointer relative flex flex-wrap gap-5 md:gap-8 xl:gap-11 items-start">
            <div class="icon relative z-10 flex overflow-hidden items-center justify-center w-[70px] h-[70px] transition-all duration-500 text-primary rounded-[50%] bg-primary bg-opacity-[0.05] before:content-[''] before:absolute before:-z-10 before:top-0 before:right-0 before:bottom-0 before:left-0 before:transition-all before:duration-500 before:transform before:opacity-0 before:rounded-[50%] before:bg-primary group-hover:before:transform group-hover:before:opacity-100 group-hover:before:rounded-full group-hover:text-white">
                <font-awesome-icon :icon="item.icon" class="text-[30px] leading-[1] flex group-hover:before:text-white" />
            </div>
            <div class="content flex-1">
              <h3 class="title text-2xl sm:text-3xl xl:text-4xl text-white">{{item.title}}</h3>
              <p class="address text-white opacity-[0.75]">{{item.subtitle}}</p>
            </div>
          </div>
        </li>
      </ul>
  
      <div class="w-full">
        <div class="map-location-layer">
          <img class="w-full" src="/images/locations/map-2.png" alt="location map">
          <div v-for="(item, index) in categories" :key="index" :id="'map-location-' + index" class="map-location-item" :style="{ left: item.left, bottom: item.bottom }">
            <span class="title" v-if="active === index">{{item.title}}</span>
          </div>
          <a class="google-map-link" :href="googleMapLink" target="_blank"><i class="fi fi-map-1 mr-2"></i>OPEN GOOGLE MAP</a>
        </div>
      </div>
  
    </div>
  </template>
  
  <script>
    import {
    faBuilding,
    faLandmark,
    faSubway,
    faShoppingBag,
    faShip,
    faTrain,
    faTrainSubway,
    faBagShopping
    } from "@fortawesome/free-solid-svg-icons";

  import { library } from "@fortawesome/fontawesome-svg-core";
  import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
  

  library.add(faBuilding, faLandmark, faSubway, faShoppingBag, faShip, faTrain, faTrainSubway, faBagShopping);
  
  export default {
    components: {
      FontAwesomeIcon
    },
    data() {
      return {
        active: 0,
        categories: [
  {
    icon: 'building',
    title: 'Sky Tower',
    left: '44%',
    bottom: '31%',
    subtitle: 'Sky Tower is the tallest residential building in the city, offering stunning panoramic views.'
  },
  {
    icon: ['fas', 'train-subway'],
    title: 'Metro (Under Construction)',
    left: '60%', // Just a placeholder, adjust as needed
    bottom: '20%', // Just a placeholder, adjust as needed
    subtitle: 'An ambitious project aimed at reducing traffic congestion, currently under construction.'
  },
  {
    icon: 'landmark',
    title: 'Jewish Holocaust Museum',
    left: '25%', // Just a placeholder, adjust as needed
    bottom: '40%', // Just a placeholder, adjust as needed
    subtitle: 'A solemn tribute to the lives lost during the Holocaust, this museum educates people on the history and implications.'
  },
  {
    icon: ['fas', 'bag-shopping'],
    title: 'Thessaloniki Mall',
    left: '70%', // Just a placeholder, adjust as needed
    bottom: '60%', // Just a placeholder, adjust as needed
    subtitle: 'The go-to place for all your shopping needs, offering a wide array of stores and entertainment.'
  },
  {
    icon: 'ship',
    title: 'Civilian Port Thessaloniki',
    left: '30%', // Just a placeholder, adjust as needed
    bottom: '15%', // Just a placeholder, adjust as needed
    subtitle: 'A bustling port connecting the city to various international destinations, perfect for a short getaway.'
  }
],

        googleMapLink: "https://www.google.com/maps/place/Litous+1,+Thessaloniki+546+27,+Greece/@40.6420884,22.9083298,17z/data=!3m1!4b1!4m6!3m5!1s0x14a83981e46202ff:0xe77a00625f4e6730!8m2!3d40.6420844!4d22.9109047!16s%2Fg%2F11n140rcd1?entry=ttu"
      };
    },
    methods: {
      activate(index) {
        this.active = index;
      }
    }
  };
  </script>
  
  <style lang="scss" scoped>
  .trigger-active {
    & .icon {
      @apply border-primary before:bg-primary before:transform before:opacity-100 before:rounded-full text-white;
    }
  }
  
  .redcolor {
    @apply text-[#F92502];
  }
  
  .map-location-layer {
    @apply relative;
  }
  
  .map-location-item {
    @apply absolute md:w-[40px] sm:w-[20px] w-[10px] md:h-[40px] sm:h-[20px] h-[10px] cursor-pointer rounded-full bg-primary shadow-[0_0_0_10px_rgba(14,164,120,0.1)];
    & .title {
      @apply text-sm whitespace-nowrap font-semibold absolute -top-[70px] left-1/2 transform -translate-x-1/2 text-black py-1 px-4 transition-all duration-500 rounded-[4px] bg-white shadow-[0_10px_40px_0_rgba(0,0,0,0.15)] before:absolute before:-bottom-6 before:left-1/2 before:w-[10px] before:h-6 before:transform before:-translate-x-1/2 before:bg-white before:content-[''];
      &::before {
        clip-path: polygon(0% 0%, 100% 0%, 50% 100%, 50% 100%, 0% 0%);
      }
    }
  }
  
  .google-map-link {
    @apply absolute bottom-1 sm:bottom-10 left-0 w-full text-center text-white text-[12px] sm:text-[15px];
  }
  </style>
  