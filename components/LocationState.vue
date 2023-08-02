<template>
    <div class="flex gap-6 items-center lg:flex-row flex-col">

        <ul class="lg:w-5/12 w-full flex flex-col gap-7 md:gap-9">
            <li class="relative" v-for="(item, index) in categories" :key="index" :class="[index === active ? 'trigger-active' : '']" @click='activate(index)'>
                <div class="cursor-pointer relative flex flex-wrap gap-5 md:gap-8 xl:gap-11 items-start">
                    <span class="icon relative w-[30px] h-[30px] transition-all duration-500 rounded-full border-1 border-bordercolor before:absolute before:top-1/2 before:left-1/2 before:w-[6px] before:h-[6px] before:conent-[''] before:transition-all before:duration-500 before:-translate-x-1/2 before:-translate-y-1/2 before:transform before:bg-[#cccccc] before:rounded-full mt-1"></span>
                    <div class="content flex-1">
                        <h3 class="title text-2xl sm:text-3xl xl:text-4xl">{{item.title}}</h3>
                        <p class="address">{{item.subtitle}}</p>
                    </div>
                </div>
            </li>
        </ul>

        <div class="lg:w-7/12 w-full">
            <div class="map-location-layer">
                <img src="/images/locations/map-1.png" loading="lazy" alt="location map" width="845" height="672">
                <div id="map-location-1" class="map-location-item active" style="top: 20%; left: 35%;">
                    <span class="title" v-if="active === 0">Gaucho Restaurant</span>
                </div>
                <div id="map-location-2" class="map-location-item" style="left: 18%; top: 45%;">
                    <span class="title" v-if="active === 1">Manhattan Hospital</span>
                </div>
                <div id="map-location-3" class="map-location-item" style="left: 28%; bottom: 25%;">
                    <span class="title" v-if="active === 2">Costco Supermarket Center</span>
                </div>
                <div id="map-location-4" class="map-location-item" style="left: 48%; top: 25%;">
                    <span class="title" v-if="active === 3">Ecostate Park</span>
                </div>
                <div id="map-location-5" class="map-location-item" style="right: 31%; bottom: 39%;">
                    <span class="title" v-if="active === 4">Harvard University</span>
                </div>
                <a class="google-map-link" href="https://www.google.com/maps/@23.1866368,89.6499712,13z" target="_blank"><i class="fi fi-map-1 mr-2"></i>OPEN GOOGLE MAP</a>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        data () {
            return {
                active: 0,
                categories: [
                    {
                        title: "Gaucho Restaurant",
                        subtitle: "1.5 Km - Restaurant"
                    },
                    {
                        title: "Manhattan Hospital",
                        subtitle: "1.8 Km - Hospital"
                    },
                    {
                        title: "Costco Supermarket Center",
                        subtitle: "3.2 Km - Supermarket"
                    },
                    {
                        title: "Ecostate Park",
                        subtitle: "3.5 Km - Park"
                    },
                    {
                        title: "Harvard University",
                        subtitle: "5.7 Km - School"
                    }
                ]
            }
        },
        methods: {
            activate(index) {
                this.active = index;
            }
        }
    }
</script>

<style lang="scss" scoped>
.trigger-active {
    // @apply before:content-[''] before:absolute before:-bottom-[10px] before:w-[30px] before:h-[30px] before:bg-white before:left-1/2 before:-translate-x-1/2 before:transform before:rotate-45;
    & .icon{
        @apply border-primary before:bg-primary;
    }
}

.redcolor{
    @apply text-[#F92502];
}
.map-location-layer{
    @apply relative -mt-0 2xl:-mt-[120px];
}
.map-location-item{
    @apply absolute w-[10px] h-[10px] cursor-pointer rounded-full bg-primary shadow-[0_0_0_10px_rgba(14,164,120,0.1)];
    & .title{
        @apply text-sm whitespace-nowrap font-semibold absolute -top-[70px] left-1/2 transform -translate-x-1/2 text-black py-1 px-4 transition-all duration-500 rounded-[4px] bg-white shadow-[0_10px_40px_0_rgba(0,0,0,0.15)] before:absolute before:-bottom-6 before:left-1/2 before:w-[10px] before:h-6 before:transform before:-translate-x-1/2 before:bg-white before:content-[''];
        &::before{
            clip-path: polygon(0% 0%, 100% 0%, 50% 100%, 50% 100%, 0% 0%);
        }
    }
}
.google-map-link{
    @apply absolute bottom-0 left-0 w-full text-center text-[#064DF0];
}
</style>