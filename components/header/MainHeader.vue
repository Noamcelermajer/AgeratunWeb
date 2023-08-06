<template>
    <!-- Header Section Start -->
    <div class="absolute top-0 left-0 right-0 z-[999]" :class="{'is-sticky': isSticky}">
        <div class="container-fluid mx-auto">
            <div class="flex justify-between items-center">
                <div class="flex items-center">
                    <Logo v-if="!isSticky" class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/home"/>
                    <LogoDark v-else class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/home"/>
                    <MainMenu :class="textClass"/>
                </div>
                    <div class="flex items-center">
                        <ButtonDefault 
                            :btnLink="'/contact'"
                            :btnClass="'btn-sm btn btn-hover-primary btn-outline-light'"
                            :btnText="'Schedule a visit'"
                            :btnClassParent="'flex'"
                            class="hidden sm:inline-flex"
                        />

                    </div>
                </div>
                <div class="flex w-full h-[1px] opacity-[0.25] bg-white"></div>
            </div>
        </div>
        <!-- Header Section End -->

</template>

<script>
export default {
    props: {
        textClass: {
            type: String,
            required: false,
        }
    },
    components: {
        Logo: () => import('@/components/logo/Logo'),
        MainMenu: () => import('@/components/header/MainMenu'),
        ButtonDefault: () => import('@/components/button/ButtonDefault')
    },
    data() {
        return {
            isSticky: false
        }
    },
    mounted() {
        window.addEventListener('scroll', this.updateStickyState);
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.updateStickyState);
    },
    methods: {
         updateStickyState() {
            let scrollPos = window.scrollY;
            if (scrollPos >= 100) {
                this.isSticky = true;
            } else {
                this.isSticky = false;
            }
        }
    
    }
}
</script>
<style lang='scss'>
.is-sticky {
    @apply bg-black transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;
    & .border-class {
        @apply hidden;
    }
}
</style>

</style>