<template>
    <div>
        <div class="flex justify-between mb-[40px] lg:mb-20 flex-col lg:flex-row gap-5">
            <div class="flex-auto w-auto">
                <span class="text-sm leading-[1.714] block uppercase text-primary">Photos & Videos Gallery</span>
            </div>
            <div class="flex-auto w-auto">
                <ul class="flex flex-wrap gap-3 sm:gap-5 lg:gap-[30px] justify-start lg:justify-end">
                    <li class="text-base lg:text-lg cursor-pointer gallery-tab-one" v-for="(tab, Index) in tabs" :key="Index" @click="currentTab = Index" :class="{active: currentTab === Index}">{{tab}}</li>
                </ul>
            </div>
        </div>
        <div class="content-bd">
            <div class="tab-content">
                <div v-if="currentTab === 0">
                    <GallerySliderAll/>
                </div>
                <div v-if="currentTab === 1">
                    <GallerySliderOne/>
                </div>
                <div v-if="currentTab === 2">
                    <GallerySliderTwo/>
                </div>
                <div v-if="currentTab === 3">
                    <GallerySliderThree/>
                </div>
                <div v-if="currentTab === 4">
                    <GallerySliderFour/>
                </div>
                <div v-if="currentTab === 5">
                    <GallerySliderFive/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        components: {
            GallerySliderAll: () => import('@/components/gallery/GallerySliderAll')
        },
        data () {
            return {
                currentTab: 0,
                tabs: ['All']
            }
        },
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
</style>