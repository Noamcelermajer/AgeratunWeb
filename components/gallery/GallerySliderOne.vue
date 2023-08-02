<template>
    <div class="galleryslider relative">
        
        <CoolLightBox 
            :items="items" 
            :index="index"
            @close="index = null">
        </CoolLightBox>
        <swiper class="swiper" :options="swiperOption">
            <swiper-slide v-for="(item, imageIndex) in items" :key="imageIndex">

                <div @click="index = imageIndex" class="relative block overflow-hidden bg-primary group cursor-pointer">
                    <img class="group-hover:opacity-40 transition duration-500 group-hover:transform w-full" :src="`${item.image}`" alt="Thumb">
                    <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                </div>

            </swiper-slide>
        </swiper>
            
        <div class="">
            <button class="prevbtn swipper-arrow bg-[url('/images/shapes/swiper-prev.png')] bg-center bg-no-repeat h-[120px] w-[28px] -left-[2px] top-1/2 absolute newstyle-arrow -translate-y-1/2 z-99">
                <i class="fa fa-chevron-left"></i>
            </button>
            <button class="nextbtn swipper-arrow bg-[url('/images/shapes/swiper-next.png')] bg-center bg-no-repeat h-[120px] w-[28px] -right-[2px] top-1/2 absolute newstyle-arrow -translate-y-1/2 z-99">
                <i class="fa fa-chevron-right"></i>
            </button>
        </div>

    </div>
</template>
<script>
    import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
    import CoolLightBox from 'vue-cool-lightbox'
    import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'
    import projects from '@/data/gallerydata.json'
    export default {
        components: {
            CoolLightBox,
            Swiper,
            SwiperSlide
        },
        data () {
            return {    
                projects,            
                swiperOption: {
                    slidesPerView: 5,
                    loop: false,
                    spaceBetween: 30,
                    pagination: false,
                    navigation: {
                        nextEl: '.galleryslider .nextbtn',
                        prevEl: '.galleryslider .prevbtn'
                    },
                    breakpoints: {
                        1680: {
                            slidesPerView: 5,
                            spaceBetween: 30
                        },
                        1025: {
                            slidesPerView: 4,
                            spaceBetween: 30
                        },
                        768: {
                            slidesPerView: 3,
                            spaceBetween: 30
                        },
                        480: {
                            slidesPerView: 2,
                            spaceBetween: 20
                        },
                        320: {
                            slidesPerView: 2,
                            spaceBetween: 10
                        }
                    }
                },
                index: null,
                items:[]
            }
        },
        mounted () {
            this.items = this.projects.filter(project=> project.categories.includes("LivingRoom"))
        }
    }
</script>
<style lang="scss" scooped>

</style>
