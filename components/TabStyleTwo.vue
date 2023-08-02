<template>
    <div>
        <ul class="flex flex-wrap mb-7 md:mb-10 lg:mb-12 gap-x-0 gap-y-5">
            <li class="md:flex-1 flex-[1_0_45%] relative" v-for="(item, index) in categories" :key="index" :class="[index === active ? 'trigger-active' : '']" @click='activate(index)'>
                <button class="xl:text-2xl lg:text-xl sm:text-lg text-sm font-bold relative flex justify-center w-full px-[10px] pb-5 xl:pb-7 cursor-pointer uppercase text-black border-b-[3px] border-[#D0CDCB] bg-transparent before:absolute before:z-10 before:right-0 before:-bottom-[3px] before:left-0 before:h-[3px] before:content-[''] before:transition-all before:duration-500 before:transform before:scale-0 before:bg-primary">{{categories[index]}}</button>
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
                                        :btnLink="'/#contact-section'"
                                        :btnClass="'btn-md min-w-[205px] text-center btn btn-primary btn-hover-dark'"
                                        :btnText="'I am interested'"
                                    />
                                </div>
                            </div>
                        </div>
                        <div class="lg:w-2/3 w-full flex-auto text-center">
                            <div class="floor-plan-image text-center flex justify-center">
                                <img :src="item.imgSrc" class="w-auto max-w-full h-auto max-h-full" alt="52.4 m2" width="965" height="776">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import tabContent from '@/data/floorplandatatwo.json'


export default {
  data () {
    return {
      active: 0,
      categories: [
        "1st Apartment",
        "2nd Apartment",
        "3rd Apartment"
      ],
      tabContent
    }
  },
  methods: {
    activate(index) {
      this.active = index;
    },
  }
}
</script>

<style lang="scss" scoped>
.trigger-active {
    & button {
        @apply before:transform before:scale-100 before:content-[''];
    }
}
.floor-plan{
    &-content{
        @apply mt-3;
    }
    &-title{
        @apply text-[32px] md:text-[40px] xl:text-5xl mb-5 leading-[1.25];
    }
    &-text{
        @apply lg:mb-10 mb-6
    }
    &-buttons{
        @apply flex gap-4 items-start 2xl:items-center 2xl:flex-row lg:flex-col sm:flex-row flex-col mt-12;
    }
}
.redcolor{
    @apply text-[#F92502];
}
</style>
