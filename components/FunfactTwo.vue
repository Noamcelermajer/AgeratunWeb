<template>
    <div class="container-fluid">
        <div class="relative section-padding pt-0" v-observe-visibility="{callback: visibilityChanged, once: true}">
            <div v-if="commentsVisible" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-x-10 xl:gap-x-24 -mb-8">
                <div v-for="(count, imageIndex) in counter" :key="imageIndex" class="counterup-two group">
                    <div class="counterup-content">
                        <countTo class="counterup-two_number relative block text-primary" :startVal='count.startVal' :endVal='count.endVal' :duration='3000' :autoplay='true'></countTo>
                        <p class="counterup-two_text text-sm lg:mt-2">{{count.text}}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class=" border-b-1 border-light opacity-[0.25]"></div>
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
                        endVal: 1520,
                        text: "Square Feet"
                    },
                    {
                        startVal: 0,
                        endVal: 6,
                        text: "Bed Room"
                    },
                    {
                        startVal: 0,
                        endVal: 4,
                        text: "Bath Room"
                    },
                    {
                        startVal: 0,
                        endVal: 2,
                        text: "Car Parking"
                    },
                    {
                        startVal: 0,
                        endVal: 1,
                        text: "Outdoor Pool"
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
    .counterup-two{
        &_number{
            @apply font-play text-[54px] md:text-7xl font-normal mb-1 sm:mb-4;
        }
        &_text{
            @apply text-sm uppercase text-[#cccccc]
        }
    }
</style>