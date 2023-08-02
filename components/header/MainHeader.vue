<template>

        <!-- Header Section Start -->
        <div class="absolute top-0 left-0 right-0 z-[999]">
            <div class="container-fluid mx-auto">
                <div class="flex justify-between items-center">
                    <div class="flex items-center">
                        <Logo class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/home"/>
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
                        <!-- Offcanvas Button Start -->
                        <div class="lg:hidden block leading-[1rem] ml-[10px] sm:ml-[15px]">
                            <button class="overflow-hidden bg-transparent h-[18px] relative w-[26px]" @click="mobiletoggleClass('addClass', 'show-mobile-menu')">
                                <span class="w-full h-[2px] bg-white block my-2 transition-all before:content-[''] before:top-0 before:bottom-auto before:absolute before:left-0 before:w-full before:h-[2px] before:bg-white after:content-[''] after:absolute after:left-0 after:w-full after:h-[2px] after:bg-white after:top-auto after:bottom-0"></span>
                            </button>
                        </div>
                        <!-- Offcanvas Button End --> 
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
    methods: {
        // offcanvas mobile-menu
        mobiletoggleClass(addRemoveClass, className) {
            const el = document.querySelector('#offcanvas-menu');
            if (addRemoveClass === 'addClass') {
                el.classList.add(className);
            } else {
                el.classList.remove(className);
            }
        }
    }
}
</script>
<style lang='scss'>

</style>