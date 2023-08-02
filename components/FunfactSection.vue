<template>
    <div class="custom-column">

        <div class="column-left">
            <div class="sidebar-text flex flex-col gap-2 lg:gap-8">
                <div class="sidebar-text-item">
                    <h6 class="text-primary text-[14px] font-normal leading-[1.7] block uppercase mb-0 lg:mb-2">begining from</h6>
                    <h5 class="text-[18px] font-semibold leading-[1.44] block">2016</h5>
                </div>
                <div class="sidebar-text-item">
                    <h6 class="text-primary text-[14px] font-normal leading-[1.7] block uppercase mb-0 lg:mb-2">completed in</h6>
                    <h5 class="text-[18px] font-semibold leading-[1.44] block">2021</h5>
                </div>
            </div>
        </div>

        <div class="column-right">
            <div class="content-block">
                <h2 class="content-block-title">Ecostate Residences is an elite residential complex located in the prestigious Manhattan's district.</h2>
                <h4 class="content-block-location"><i class="fi fi-maps-and-flags"></i>Payson Ave. &amp;, Seaman Ave, Manhattan, NY</h4>
            </div>
            <div class="relative" v-observe-visibility="{callback: visibilityChanged, once: true}">
                <div v-if="commentsVisible" class="grid md:grid-cols-2 grid-cols-1 gap-x-10 xl:gap-x-24 -mb-8">
                    <div v-for="(count, imageIndex) in counter" :key="imageIndex" class="counterup group">
                        <div class="counterup-icon relative z-10 flex overflow-hidden items-center justify-center w-[85px] h-[85px] transition-all duration-500 text-[#3F3C3C] rounded-[50%] bg-[#F3F3F9] before:content-[''] before:absolute before:-z-10 before:top-0 before:right-0 before:bottom-0 before:left-0 before:transition-all before:duration-500 before:transform before:bg-opacity-0 before:ruonded-[50%] before:bg-primary group-hover:before:transform group-hover:before:bg-opacity-100 group-hover:before:rounded-full group-hover:text-white"><i class="text-[40px] leading-[1] flex" :class="count.icoClass"></i></div>
                        <div class="counterup-content">
                            <countTo class="counterup_number text-[40px] md:text-5xl font-bold relative block mb-1 text-primary" :startVal='count.startVal' :endVal='count.endVal' :duration='3000' :autoplay='true'></countTo>
                            <p class="counterup_text text-sm mt-2">{{count.text}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import countTo from 'vue-count-to';
    export default {
        components: {
            countTo
        },
        data () {
            return {
                commentsVisible: false,
                counter: [
                    {
                        startVal: 0,
                        endVal: 15000,
                        icoClass: "fi fi-select",
                        text: "Square Feet"
                    },
                    {
                        startVal: 0,
                        endVal: 250,
                        icoClass: "fi fi-apartment-3",
                        text: "Apartments"
                    },
                    {
                        startVal: 0,
                        endVal: 5,
                        icoClass: "fi fi-apartment-1",
                        text: "Blocks of Flats"
                    },
                    {
                        startVal: 0,
                        endVal: 1050,
                        icoClass: "fi fi-car-park",
                        text: "Slot Car Parking"
                    }
                ]
            }
        },
        methods: {
            visibilityChanged(isVisible) {
                this.commentsVisible = isVisible;
            },
        }
    }
</script>

<style lang="scss">
    .custom-column{
        @apply flex flex-col lg:gap-y-0 md:gap-y-8 gap-y-6 lg:flex-row justify-between;
    }
    .column-left{
        @apply lg:w-[315px] xl:w-[375px] 2xl:w-[441px] max-w-full flex-shrink-0;
    }
    .column-right {
        @apply lg:w-[calc(100%-315px)] xl:w-[calc(100%-375px)] 2xl:w-[calc(100%-441px)] max-w-full;
    }
    .content-block {
        @apply mb-14;
        &-title {
            @apply text-[24px] sm:text-[30px] md:text-[36px] mb-7 md:mb-10;
        }
        &-location {
            @apply block relative text-lg md:text-xl font-semibold leading-[1.5] pl-9;
            & i {
                @apply absolute left-0 top-[2px];
            }
        }
    }
    .counterup{
        @apply flex items-center flex-wrap gap-9 py-8 border-t-1 border-bordercolor;
    }
</style>