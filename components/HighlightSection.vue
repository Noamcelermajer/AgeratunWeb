<template>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 grid-cols-1 gap-x-12 -mb-8">
        <div v-for="(highlight, imageIndex) in allitems" :key="imageIndex" class="highlight group">
            <div class="highlight-icon relative z-10 flex overflow-hidden items-center justify-center w-[85px] h-[85px] transition-all duration-500 text-primary rounded-[50%] bg-primary bg-opacity-[0.05] before:content-[''] before:absolute before:-z-10 before:top-0 before:right-0 before:bottom-0 before:left-0 before:transition-all before:duration-500 before:transform before:opacity-0 before:ruonded-[50%] before:bg-primary group-hover:before:transform group-hover:before:opacity-100 group-hover:before:rounded-full group-hover:text-white">
                <i class="text-[40px] leading-[1] flex" :class="highlight.icoClass"></i>
            </div>
            <div class="highlight-content">
                <h3 class="highlight_title text-[40px] md:text-5xl font-bold relative block mb-1 text-primary">{{highlight.title}}</h3>
                <p class="highlight_text text-sm mt-2">{{highlight.text}}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
        data () {
            return {
                allitems: [
                    {
                        title: "Phone & Reception",
                        icoClass: "fi fi-phone-call",
                        text: "receptionist serve 24/7"
                    },
                    {
                        title: "Managing Application",
                        icoClass: "fi fi-shield",
                        text: "Application to monitor apartement availability"
                    },
                    {
                        title: "Fire Alarm",
                        icoClass: "fi fi-notification",
                        text: "Automatic fire extinguishing system in each apartment"
                    },
                    {
                        title: "Car Parking",
                        icoClass: "fi fi-car-park",
                        text: "The parking area with the capacity more than 20,000 slots car parking"
                    },
                    {
                        title: "Air Conditioner",
                        icoClass: "fi fi-line-1",
                        text: "Ensure ventilation & air circulation in your home with air conditioning system"
                    },
                    {
                        title: "Spa and Gym",
                        icoClass: "fi fi-spa",
                        text: "Take care your health with Spa & Equipped gym"
                    },
                    {
                        title: "Outdoor Pool",
                        icoClass: "fi fi-water-waves",
                        text: "rooftop swimming pool system"
                    }
                ]
            }
        },
}
</script>

<style lang="scss">
    .highlight{
        @apply  flex items-center flex-wrap gap-9 py-8 border-t-1 border-bordercolor;
        &-content{
            @apply  w-[calc(100%-122px)];
        }
        &_title{
            @apply text-2xl font-bold relative block mb-[6px] text-black;
        }
        &_text{
            @apply text-sm text-dark;
        }
    }
</style>