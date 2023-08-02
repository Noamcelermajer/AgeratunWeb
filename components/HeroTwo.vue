<template>
    <!-- Hero Slider Section Start -->
    <div class="herotwo">
        <div class="herotwo-bg"></div>
        <div class="container-fluid mx-auto">
            <div class="flex lg:flex-row flex-col gap-10">
                <div class="lg:w-1/2 w-full self-center">
                    <h2 class="herotwo-title"> Sky Tower</h2>
                    <div class="herotwo-signature">
                    </div>
                    <h4 class="herotwo-location"><i class="fi fi-maps-and-flags"></i>Litous 1, Thessaloniki 546 27, Greece</h4>
                </div>
                <div class="lg:w-1/2 w-full flex lg:justify-end">
                    <div class="relative z-10 block w-full max-w-[490px] p-10 sm:p-[70px]">
                        <div class="absolute -z-10 top-0 right-0 bottom-0 left-0">
                            <img class="w-full h-full object-cover" src="images/shapes/price-box.png" alt="Pricing-Shape" style="opacity:0.4;filter:alpha(opacity=40);">
                        </div>
                        <h6 class="block text-base font-semibold mb-7 sm:mb-12 uppercase text-white">Initial Price</h6>
                        <h2 class="block font-play text-[54px] sm:text-[84px] font-normal leading-[1.071] relative mb-5 sm:mb-6 text-[#FFCA3B]">89,000€</h2>
                        <h3 class="sm:text-[30px] text-xl font-normal relative block mb-12 sm:mb-[53px] text-white">Tax Included</h3>
                        <div class="block w-full mb-9 sm:mb-12">
                            <ButtonDefault 
                                :btnLink="'/contact'"
                                :btnClass="'min-h-[50px] md:min-h-[60px] lg:min-h-[70px] py-2 sm:py-5 btn relative overflow-hidden h-[54px] lg:h-[60px] px-[30px] lg:px-[40px] text-base sm:text-[18px] font-bold btn-primary flex items-center justify-center btn-hover-light w-full'"
                                :btnText="'Take a Tour'"
                                :btnIcon="'!hidden'"
                                :btnClassParent="'block leading-[1] text-center'"
                            />
                        </div>
                        <div class="relative block pl-16">
                            <span class="text-xs leading-1 absolute top-0 left-0 uppercase text-white">call<br>direct </span>
                            <a class="sm:text-2xl text-xl font-normal leading-7 text-white" href="tel:+5435682625">050000000</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Hero Slider Section End -->
</template>

<script>
    export default {
        components: {
        },
        data() {
            return {
            }
        }
    }
</script>

<style lang="scss" scoped>
.herotwo {
    @apply relative z-10 pt-[120px] sm:pt-[150px] md:pt-[200px] md:pb-[150px] sm:pb-[100px] pb-16 lg:py-[200px] 2xl:py-[270px];
    &-bg{
        @apply absolute -z-20 top-0 right-0 -bottom-[4px] left-0 bg-no-repeat bg-fixed bg-center bg-cover bg-[url('/images/hero/Rooftop.png')] before:absolute before:top-0 before:left-0 before:w-full before:h-full before:content-[''] ;
        &::before{
            background: linear-gradient(0deg, #221f1e 0.5%, rgba(0, 0, 0, 0.5) 5%);
        }
    }
    &-title {
        @apply font-normal leading-[.85] uppercase text-white text-[70px] sm:text-[110px] md:text-[140px] lg:text-[110px] xl:text-[140px] 2xl:text-[180px] font-play mb-0;
    }
    &-signature{
        @apply block max-w-[220px] sm:max-w-[290px] xl:max-w-full;
    }
    &-location{
        @apply text-lg xl:text-xl font-semibold relative inline-flex py-5 xl:py-[23px] pr-[30px] pl-[60px] xl:pl-[80px] text-white bg-black bg-opacity-60;
        & i {
            @apply absolute top-1/2 left-9 -translate-y-1/2;
        }
    }
}
</style>