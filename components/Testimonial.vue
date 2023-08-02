<template>
    <div class="custom-column">

        <div class="column-left">
            <div class="sidebar-text flex flex-col gap-8">
                <div class="sidebar-text-item">
                    <h6 class="text-primary text-[14px] font-normal leading-[1.7] block uppercase">Residential Community</h6>
                </div>
            </div>
        </div>

        <div class="column-right">
            <swiper class="swiper testimonial" :options="swiperOption">
                <swiper-slide>
                    <div class="testimonial-text">
                        <h5 class="content-block-title">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</h5>
                    </div>
                    <div class="testimonial-author flex flex-wrap gap-6 items-center pt-0 lg:pt-5">
                        <div class="testimonial-author-thumb">
                            <img src="images/testimonial/testimonial-1.jpg" loading="lazy" width="60" height="60" alt="MartinL">
                        </div>
                        <div class="testimonial-author-content">
                            <h6 class="testimonial-author-name mb-0 text-lg">Thiago A.</h6>
                            <span class="testimonial-author-designation text-sm">Block A Resident</span>
                        </div>
                    </div>
                </swiper-slide>
                <swiper-slide>
                    <div class="testimonial-text">
                        <h5 class="content-block-title">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</h5>
                    </div>
                    <div class="testimonial-author flex flex-wrap gap-6 items-center pt-0 lg:pt-5">
                        <div class="testimonial-author-thumb">
                            <img src="images/testimonial/testimonial-2.jpg" loading="lazy" width="60" height="60" alt="MartinL">
                        </div>
                        <div class="testimonial-author-content">
                            <h6 class="testimonial-author-name mb-0 text-lg">McGregor C.</h6>
                            <span class="testimonial-author-designation text-sm">Block A Resident</span>
                        </div>
                    </div>
                </swiper-slide>
                <swiper-slide>
                    <div class="testimonial-text">
                        <h5 class="content-block-title">“The difference in life that I found in Ecostate is the warmth of family affection. I feel very happy when I come home, this place has helped my family members spend more and more time together and the affection is also stronger. Thank you very much Ecostate.”</h5>
                    </div>
                    <div class="testimonial-author flex flex-wrap gap-6 items-center pt-0 lg:pt-5">
                        <div class="testimonial-author-thumb">
                            <img src="images/testimonial/testimonial-3.jpg" loading="lazy" width="60" height="60" alt="MartinL">
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
                    slidesPerView: 1,
                    loop: true,
                    spaceBetween: 30,
                    pagination: {
                        el: '.swiper-pagination',
                        clickable: true,
                        type: 'bullets'
                    }
                }
            }
        }
    }
</script>

<style lang="scss">
.default-pagination{
    @apply md:gap-5 gap-3 flex mt-10;
    & .swiper-pagination-bullet{
        @apply w-[10px] h-[10px] bg-[#cccccc] opacity-100;

        &.swiper-pagination-bullet-active{
            @apply bg-primary;
        }
    }
}
</style>