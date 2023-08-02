<template>
    <div class="custom-column">

        <div class="column-left">
            <div class="sidebar-text flex flex-col gap-8">
                <div class="sidebar-text-item">
                    <h6 class="text-primary text-[14px] font-normal leading-[1.7] block uppercase">Sky Tower Features</h6>
                </div>
            </div>
        </div>

        <div class="column-right">
            <div class="content-block">
                <h2 class="content-block-title">20+ Premium and essential services in Sky Tower Park, contributing to enhancing residents' life experience</h2>
            </div>
            <div class="relative">
                <div class="grid md:grid-cols-2 grid-cols-1 gap-6 lg:gap-10">
                    <div v-for="(feature, imageIndex) in featureData" :key="imageIndex" class="group flex gap-9 items-center max-w-[450px]">
                        <div class="shrink-0 relative z-10 flex overflow-hidden items-center justify-center w-[85px] h-[85px] transition-all duration-500 text-[#3F3C3C] rounded-full bg-[#F3F3F9] before:content-[''] before:absolute before:-z-10 before:top-0 before:right-0 before:bottom-0 before:left-0 before:transition-all before:duration-500 before:transform before:ruonded-[50%] before:bg-opacity-0 before:bg-primary group-hover:before:transform group-hover:before:rounded-full group-hover:text-white group-hover:before:bg-opacity-100"><i class="text-[40px] leading-[1] flex" :class="feature.icoClass"></i></div>
                        <div class="counterup-content">
                            <h3 class="text-2xl font-bold relative block mb-1 text-primary">{{feature.title}}</h3>
                            <p class="text-sm mt-2">{{feature.text}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import featureData from '@/data/featuredata.json'
    export default {
        data () {
            return {
                featureData
            }
        }
    }
</script>

<style lang="scss">

</style>