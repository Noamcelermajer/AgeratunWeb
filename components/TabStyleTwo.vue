<template>
    <div>
        <ul class="flex flex-wrap mb-7 md:mb-10 lg:mb-12 gap-x-0 gap-y-5">
            <li class="md:flex-1 flex-[1_0_45%] relative" v-for="(item, index) in categories" :key="index" :class="[index === active ? 'trigger-active' : '']" @click='activate(index)'>
                <button class="xl:text-2xl lg:text-xl sm:text-lg text-sm font-bold relative flex justify-center w-full px-[10px] pb-5 xl:pb-7 cursor-pointer uppercase text-black border-b-[3px] border-[#D0CDCB] bg-transparent before:absolute before:z-10 before:right-0 before:-bottom-[3px] before:left-0 before:h-[3px] before:content-[''] before:transition-all before:duration-500 before:transform before:scale-0 before:bg-primary">{{categories[index]}}</button>
            </li>
        </ul>

        <div v-for="(item, index) in tabContent" :key="index">
            <div class="" v-if="active === item.tabNumber">
                <div class="floor-plan">
                    <div class="flex gap-6 lg:flex-row flex-col">
                        <div class="lg:w-1/3 w-full flex-auto">
                            <div class="floor-plan-content">
                                <h2 class="floor-plan-title">{{item.title}}</h2>
                                <div class="floor-plan-text">
                                    <p>{{item.text}}</p>
                                </div>
                                <ul class="floor-plan-info">
                                    <li v-for="(item, index) in item.contentList" :key="index" class="text-lg relative flex justify-between py-3 text-black border-b-1 border-[#cfcfd4] last:border-b-0">{{item.listLeft}}<span :class="item.colorClass">{{item.listRight}}</span></li>
                                </ul>
                                <div class="floor-plan-buttons">
                                    <ButtonDefault 
                                        :btnClass="'btn-md min-w-[205px] text-center btn btn-primary btn-hover-dark'"
                                        :btnText="'I am interested'"
                                        @click="$emit('scroll-to-section')"
                                    />
                                    <ButtonDefault 
                                    :btnClass="'btn-md min-w-[205px] text-center btn btn-primary btn-hover-dark'"
                                    :btnText="'Show VR Demo'"
                                    @click="openIframe(item.iframeSrc)"
                                  />
                                </div>
                            </div>
                        </div>
                        <div class="lg:w-2/3 w-full flex-auto text-center">
                            <div class="floor-plan-image text-center flex justify-center">
                                <img :src="item.imgSrc" class="w-auto max-w-full h-auto max-h-full" alt="52.4 m2" width="965" height="776">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="showIframe" class="iframe-popup">
            <button @click="closeIframeAndRedirect" class="close-button">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 close-button-svg">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>
            <button @click="toggleFullscreen" class="fullscreen-button">
                <svg v-if="isFullscreen" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 fullscreen-button-svg">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 fullscreen-button-svg">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
                </svg>
            </button>
            <iframe :src="iframeSrc" style="width: 100%; height: 100%;"></iframe>
        </div>
        
    </div>
</template>

<script>
import tabContent from '@/data/floorplandatatwo.json'

export default {
  data () {
    return {
      active: 0,
      showIframe: false,
      iframeSrc: '',
      isFullscreen: false,
      categories: [
        "1st Apartment",
        "2nd Apartment",
        "3rd Apartment"
      ],
      tabContent
    }
  },
  methods: {
    activate(index) {
      this.active = index;
    },
    openIframe(src) {
      this.showIframe = true;
      this.iframeSrc = src;
      document.body.style.overflow = 'auto';

    },
    closeIframeAndRedirect() {
      this.showIframe = false;
      this.$router.push('/');
    },
    toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
        this.isFullscreen = true;
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
          this.isFullscreen = false;
        }
      }
    },
  }
}
</script>

<style lang="scss" scoped>
.trigger-active {
    & button {
        @apply before:transform before:scale-100 before:content-[''];
    }
}
.floor-plan{
    &-content{
        @apply mt-3;
    }
    &-title{
        @apply text-[32px] md:text-[40px] xl:text-5xl mb-5 leading-[1.25];
    }
    &-text{
        @apply lg:mb-10 mb-6
    }
    &-buttons{
        @apply flex gap-4 items-start 2xl:items-center 2xl:flex-row lg:flex-col sm:flex-row flex-col mt-12;
    }
}
.redcolor{
    @apply text-[#F92502];
}
.iframe-popup {
    background: #515151;

    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.5);
    z-index: 10000; /* add a high value to ensure the iframe appears on top */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    
}
.close-button {
    position: absolute;
    top: 10px;
    left: 10px; /* changed from right to left */
    background: none;
    border: none;
}

.close-button-svg, .fullscreen-button-svg {
    width: 30px;
    height: 30px;
}

.fullscreen-button {
    position: absolute;
    top: 10px;
    right: 10px; /* already on the right */
    background: none;
    border: none;
}
</style>
