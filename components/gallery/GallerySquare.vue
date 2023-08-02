<template>
    <div class="container-fluid">
        <div class="section-padding pt-0 border-b-1 border-bordercolor">
            <ul class="flex flex-wrap gap-3 sm:gap-5 lg:gap-[30px] justify-start mb-[50px] lg:mb-20">
                <li class="text-base lg:text-lg cursor-pointer gallery-tab-one" v-for="(tab, Indextab) in tabs" :key="Indextab" @click="currentTab = Indextab" :class="{active: currentTab === Indextab}"> {{tab}} </li>
            </ul>
            <div class="content-bd">
                <div class="tab-content">
                    <div v-if="currentTab === 0">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="items" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in items" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="currentTab === 1">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="itemstwo" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in itemstwo" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="currentTab === 2">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="itemsthree" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in itemsthree" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="currentTab === 3">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="itemsfour" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in itemsfour" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="currentTab === 4">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="itemsfive" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in itemsfive" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="currentTab === 5">
                        <div class="galleryslider relative">
                            <CoolLightBox 
                                :items="itemssix" 
                                :index="index"
                                @close="index = null">
                            </CoolLightBox>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div v-for="(item, imageIndex) in itemssix" :key="imageIndex">

                                    <div @click="index = imageIndex" class="gallery-gradient relative block overflow-hidden bg-black z-10 group cursor-pointer hover:before:opacity-100 before:absolute before:content-[''] before:top-0 before:left-0 before:right-0 before:bottom-0 before:transition-all before:duration-500 before:opacity-0 before:z-10">
                                        <img class="w-full transition duration-500 group-hover:transform" :src="`${item.imageSquare}`" alt="Thumb">
                                        <h6 class="absolute z-30 bottom-0 left-0 w-full m-0 pl-6 transition-all duration-500 opacity-0 text-white text-[15px] group-hover:opacity-100 group-hover:bottom-5">{{item.title}}</h6>
                                        <span class="text-xl video-icon absolute top-1/2 left-1/2 items-center justify-center w-20 md:w-[120px] h-20 md:h-[120px] -translate-x-1/2 -translate-y-1/2 text-white rounded-full bg-black/50 hidden" :class="item.videobtnshow"><i class="fa fa-play"></i></span>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import CoolLightBox from 'vue-cool-lightbox'
    import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'
    import projects from '@/data/gallerytwodata.json'
    export default {
        components: {
            CoolLightBox
        },
        data () {
            return {
                currentTab: 0,
                tabs: ['All', 'Living Room', 'Bed Room', 'Bath Room', 'Basement', 'Kitchen'],
                projects,
                index: null,
                items:[],
                itemstwo:[],
                itemsthree:[],
                itemsfour:[],
                itemsfive:[],
                itemssix:[]
            }
        },
        mounted () {
            this.items = this.projects.filter(project=> project.categories),
            this.itemstwo = this.projects.filter(project=> project.categories.includes("LivingRoom")),
            this.itemsthree = this.projects.filter(project=> project.categories.includes("BedRoom")),
            this.itemsfour = this.projects.filter(project=> project.categories.includes("BathRoom")),
            this.itemsfive = this.projects.filter(project=> project.categories.includes("Basement")),
            this.itemssix = this.projects.filter(project=> project.categories.includes("Kitchen"))
        }
    }
</script>

<style lang="scss">
.videobtn-show{
    @apply flex;
}
.gallery-tab-one{
    &.active{
        @apply text-primary;
    }
}
.gallery-gradient{
    &::before{
        background-image: linear-gradient(0deg, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0) 100%);
    }
}
</style>