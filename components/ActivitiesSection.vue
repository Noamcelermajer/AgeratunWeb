<template>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10 lg:gap-16 xl:gap-20">
        <div class="advantage-block group" v-for="(item, index) in activitiesData" :key="index">
            <div class="advantage-block-image relative overflow-hidden bg-primary">
                <img class="group-hover:opacity-40 group-hover:transform group-hover:transition-all group-hover:duration-500 transition-all duration-500" :src="item.image" alt="Sport and Leisure">
            </div>
            <div class="advantage-block-content pt-7 lg:pt-[35px]">
                <h2 class="lg:text-[36px] text-[24px] mb-3">{{item.title}}</h2>
                <p class="lg:mb-[45px] mb-8">{{item.text}}</p>
                <ButtonDefault 
                    :btnLink="'/'"
                    :btnClass="'btn-md min-w-[160px] btn text-center btn-transparent btn-outline-black btn-hover-primary'"
                    :btnText="'Explore'"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import activitiesData from '@/data/activitiesdata.json'
    export default {
        data () {
            return {
                activitiesData,
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>