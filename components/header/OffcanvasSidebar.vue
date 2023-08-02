<template>
    <div class="popup-mobile-menu popup-mobile-visiable" id="offcanvas-menu">
        <div class="mobile-menu-overlay" @click="mobiletoggleClass('removeClass', 'show-mobile-menu')"></div>
        <div class="bg-black w-[300px] sm:w-[400px] h-full right-auto sm:left-[calc(100%-400px)] left-[calc(100%-300px)] top-0 relative text-left transition-all pt-[25px] overflow-y-auto">

            <div class="flex justify-between px-5 pb-5 items-center border-b-1 border-white border-opacity-[0.15]">
                <div class="max-w-[180px]">
                    <n-link to="/">
                        <img src="/images/logo/logo-dark.svg" alt="Logo">
                    </n-link>
                </div>
                <button class="grid h-5 w-5 relative group" @click="mobiletoggleClass('removeClass', 'show-mobile-menu')">
                    <span class="before:content-[''] before:h-5 before:w-[3px] before:bg-white before:absolute before:top-0 before:left-1/2 before:transform before:rotate-45 relative after:content-[''] after:h-5 after:w-[3px] after:bg-white after:absolute after:top-0 after:left-1/2 after:transform after:-rotate-45 group-hover:before:bg-primary group-hover:before:transition-all group-hover:after:bg-primary group-hover:after:transition-all"></span>
                </button>
            </div>

            <div class="menu-content">
                <MobileMenu />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    components: {
        MobileMenu: () => import('@/components/header/MobileMenu'),
    },
    data() {
        return {
        }
    },
    methods: {
        mobiletoggleClass(addRemoveClass, className) {
            const el = document.querySelector('#offcanvas-menu');
            if (addRemoveClass === 'addClass') {
                el.classList.add(className);
            } else {
                el.classList.remove(className);
            }
        },
        scrollHanle(evt) {
            
        },
    },
};
</script>
<style lang="scss" scoped>
    .popup-mobile-menu {
        @apply fixed top-0 left-full w-full h-screen invisible opacity-0 transition-all;
    }
    .show-mobile-menu {
        @apply opacity-100 visible left-0 transition-all duration-500 z-9999;
        & .mobile-menu-overlay {
            @apply absolute w-full h-full bg-black bg-opacity-80 cursor-not-allowed transition-all delay-300 duration-300;
        }
    }
</style>