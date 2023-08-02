<template>
    <!-- Hero Slider Section Start -->
    <div class="hero-slider group overflow-hidden">
        <swiper class="swiper" :options="swiperOption">
            <!-- Hero Slide Item Start -->
            <swiper-slide class="hero-slide" v-for="(slide, imageIndex) in sliderData" :key="imageIndex">

                <!-- Hero Slide BG Start -->
                <div class="hero-slide-bg">
                    <img :src="slide.sliderBg" alt="Luxury Residence">
                </div>
                <!-- Hero Slide BG End -->

                <!-- Hero Slide Content Start -->
                <div class="container-fluid w-full">
                    <div class="hero-slide-content">
                        <h3 class="hero-slide-sub-title animation-one inline-flex"><span>{{slide.subtitle}}</span></h3>
                        <h2 class="hero-slide-title animation-two"><span>{{slide.titleTop}} <br>{{slide.titleBottom}}</span></h2>
                        <div class="hero-slide-btn animation-three">
                            <ButtonDefault
                                :btnLink="'/booking'"
                                :btnClass="'min-w-[205px] min-h-[50px] md:min-h-[60px] lg:min-h-[70px] py-2 sm:py-5 btn text-center relative overflow-hidden h-[54px] lg:h-[60px] px-[30px] lg:px-[40px] text-[14px] flex items-center gap-2 btn-light btn-hover-primary'"
                                :btnText="'Explore 3d vR'"
                                :btnIcon="'fi fi-model'"
                                :btnClassParent="'inline-flex leading-[1]'"
                            />
                        </div>
                    </div>
                </div>
                <!-- Hero Slide Content End -->

            </swiper-slide>
            <!-- Hero Slide Item End -->
        </swiper>
    </div>
    <!-- Hero Slider Section End -->
</template>

<script>
    import sliderData from '@/data/herosliderdata.json'
    import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
    export default {
        components: {
            Swiper,
            SwiperSlide
        },
        data() {
            return {
                swiperOption: {
                    slidesPerView: 1,
                    loop: true,
                    autoplay: {
                        delay: 4000,
                    },
                    spaceBetween: 0,
                    pagination: false,
                    effect: 'fade',
                    fadeEffect: {
                        crossFade: true
                    }
                },
                sliderData
            }
        }
    }
</script>

<style lang="scss" scoped>

.hero-slider{
    .swiper-slide-active{
        .animation-one {
            @apply opacity-100 transform translate-x-0 transition-all delay-700 duration-1000;
        }
        .animation-two {
            @apply opacity-100 transform translate-x-0 transition-all delay-1000 duration-1000;
        }
        .animation-three {
            @apply opacity-100 transform translate-x-0 transition-all delay-[1.3s] duration-1000;
        }
    }
    & .animation-one, & .animation-two, & .animation-three {
        @apply transition-all transform translate-x-[100px] opacity-0 duration-1000;
    }
}

.hero-slide {
    @apply relative flex items-center h-[450px] sm:h-[550px] md:h-[650px] lg:h-[850px] 2xl:h-[1150px] pt-[100px] md:pt-[120px] pb-[30px] md:pb-[50px] 2xl:pb-[100px] after:content-[""] z-[1] after:w-full after:h-full after:z-10 after:top-0 after:right-0 after:left-0 after:bg-[#000000] after:opacity-40 after:absolute;
    &-sub-title {
        @apply xl:text-[30px] text-[18px] sm:text-[20px] md:text-[24px] text-white font-bold mb-5 md:mb-[35px];
    }
    &-title {
        @apply leading-[0.9] mb-10 md:mb-[60px] lg:mb-[90px] -ml-[5px] lg:-ml-[12px] uppercase text-white text-[45px] sm:text-[70px] md:text-[100px] lg:text-[150px] 2xl:text-[200px] font-bold;
    }
    &.swiper-slide-active {
        & .hero-slide-bg {
            @apply transform transition-all duration-[6s];
        }
    }
    & .hero-slide-bg {
        @apply absolute -z-[1] top-0 right-0 bottom-0 left-0 transition-all duration-[6s];
        & img {
            @apply object-cover w-full h-full;
        }
    }
    &-content{
        @apply z-999 relative;
    }
}
</style>