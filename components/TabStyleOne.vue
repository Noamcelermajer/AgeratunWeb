<template>
    <div>

        <ul class="flex flex-wrap mb-12 gap-6 md:gap-1">
            <li class="md:flex-1 flex-[1_0_30%] relative" v-for="(item, index) in categories" :key="index" :class="[index === active ? 'trigger-active' : '']" @click='activate(index)'>
                <button class="bg-[#E9E9F0] lg:text-[20px] xl:text-[24px] 2xl:text-[30px] font-bold leading-10 relative z-10 flex justify-center w-full py-1 sm:py-3 lg:py-5 xl:py-8 px-4 cursor-pointer text-black border-0">{{categories[index]}}</button>
            </li>
        </ul>

        <div v-for="(item, index) in tabContent" :key="index">
            <div class="" v-if="active === item.tabNumber">
                <div class="floor-plan">
                    <div class="flex gap-6 lg:flex-row flex-col">
                        <div class="lg:w-1/3 w-full flex-auto">
                            <div class="floor-plan-content">
                                <h2 class="floor-plan-title">{{item.title}}</h2>
                                <div class="floor-plan-text">
                                    <p>{{item.text}}</p>
                                </div>
                                <ul class="floor-plan-info">
                                    <li v-for="(item, index) in item.contentList" :key="index" class="text-lg relative flex justify-between py-3 text-black border-b-1 border-[#cfcfd4] last:border-b-0">{{item.listLeft}}<span :class="item.colorClass">{{item.listRight}}</span></li>
                                </ul>
                                <div class="floor-plan-buttons">
                                    <ButtonDefault 
                                        :btnLink="'/booking'"
                                        :btnClass="'btn-md min-w-[205px] text-center btn btn-primary btn-hover-dark'"
                                        :btnText="'I am interested'"
                                    />
                                    <ButtonDefault 
                                        :btnLink="'/booking'"
                                        :btnClass="'btn-md min-w-[205px] btn text-center btn-light btn-hover-primary'"
                                        :btnText="'Explore 3d vR'"
                                        :btnIcon="'fi fi-model'"
                                    />
                                </div>
                            </div>
                        </div>
                        <div class="lg:w-2/3 w-full flex-auto">
                            <div class="floor-plan-image">
                                <img :src="item.imgSrc" class="w-full" alt="52.4 m2">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import tabContent from '@/data/floorplandata.json'
    export default {
        data () {
            return {
                active: 0,
                categories: [
                    "Studio",
                    "2 Rooms",
                    "3 Rooms",
                    "Penthouse",
                    "Double Height"
                ],
                tabContent
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
    @apply before:content-[''] before:absolute before:-bottom-[10px] before:w-[30px] before:h-[30px] before:bg-white before:left-1/2 before:-translate-x-1/2 before:transform before:rotate-45;
    button{
        @apply bg-white;
    }
}
.floor-plan{
    &-content{
        @apply mt-3;
    }
    &-title{
        @apply text-[40px] xl:text-5xl mb-5 leading-[1.25];
    }
    &-text{
        @apply mb-10
    }
    &-buttons{
        @apply flex gap-4 items-start 2xl:items-center 2xl:flex-row lg:flex-col sm:flex-row flex-col mt-12;
    }
}
.redcolor{
    @apply text-[#F92502];
}
</style>