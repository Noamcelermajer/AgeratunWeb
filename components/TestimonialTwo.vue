<template>
    <div class="container-fluid">
        <swiper class="swiper testimonial" :options="swiperOption">
            <swiper-slide>
                <div class="testimonial-text pt-9 md:pt-[60px] border-t-1 border-primary">
                    <p class="sm:text-2xl text-xl font-normal block text-black leading-[1.5]">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</p>
                </div>
                <div class="testimonial-author flex flex-wrap gap-6 items-center pt-5 lg:pt-12">
                    <div class="testimonial-author-thumb">
                        <img src="images/testimonial/testimonial-1.jpg" alt="MartinL">
                    </div>
                    <div class="testimonial-author-content">
                        <h6 class="testimonial-author-name mb-0 text-lg">Thiago A.</h6>
                        <span class="testimonial-author-designation text-sm">Block A Resident</span>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="testimonial-text pt-9 md:pt-[60px] border-t-1 border-primary">
                    <p class="sm:text-2xl text-xl font-normal block text-black leading-[1.5]">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</p>
                </div>
                <div class="testimonial-author flex flex-wrap gap-6 items-center pt-5 lg:pt-12">
                    <div class="testimonial-author-thumb">
                        <img src="images/testimonial/testimonial-2.jpg" alt="MartinL">
                    </div>
                    <div class="testimonial-author-content">
                        <h6 class="testimonial-author-name mb-0 text-lg">McGregor C.</h6>
                        <span class="testimonial-author-designation text-sm">Block A Resident</span>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="testimonial-text pt-9 md:pt-[60px] border-t-1 border-primary">
                    <p class="sm:text-2xl text-xl font-normal block text-black leading-[1.5]">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</p>
                </div>
                <div class="testimonial-author flex flex-wrap gap-6 items-center pt-5 lg:pt-12">
                    <div class="testimonial-author-thumb">
                        <img src="images/testimonial/testimonial-3.jpg" alt="MartinL">
                    </div>
                    <div class="testimonial-author-content">
                        <h6 class="testimonial-author-name mb-0 text-lg">Martin L.</h6>
                        <span class="testimonial-author-designation text-sm">Block A Resident</span>
                    </div>
                </div>
            </swiper-slide>
        </swiper>
        <!-- Add Pagination -->
        <div class="swiper-pagination default-pagination !relative"></div>
    </div>
</template>

<script>
    import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
    export default {
        components: {
            Swiper,
            SwiperSlide
        },
        data() {
            return {
                swiperOption: {
                    slidesPerView: 2,
                    loop: true,
                    spaceBetween: 50,
                    pagination: {
                        el: '.swiper-pagination',
                        clickable: true,
                        type: 'bullets'
                    },
                    breakpoints: {
                        1680: {
                            slidesPerView: 2,
                            spaceBetween: 30
                        },
                        1025: {
                            slidesPerView: 2,
                            spaceBetween: 30
                        },
                        768: {
                            slidesPerView: 2,
                            spaceBetween: 30
                        },
                        480: {
                            slidesPerView: 1,
                            spaceBetween: 20
                        },
                        320: {
                            slidesPerView: 1,
                            spaceBetween: 10
                        }
                    }
                }
            }
        }
    }
</script>

<style lang="scss">
.default-pagination{
    @apply md:gap-5 gap-3 flex justify-center mt-10;
    & .swiper-pagination-bullet{
        @apply w-[10px] h-[10px] bg-[#cccccc] opacity-100;

        &.swiper-pagination-bullet-active{
            @apply bg-primary;
        }
    }
}
</style>