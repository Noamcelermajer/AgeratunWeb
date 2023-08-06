<template>
    <div>

        <!-- Header Section Start -->
        <div class="relative top-0 left-0 right-0 z-[999]" :class="{'is-sticky': isSticky}">
            <div class="container-fluid mx-auto">
                <div class="flex justify-between items-center">
                    <div class="flex items-center">
                        <LogoDark class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/"/>
                        <MainMenu :textClass="'text-black sticky-height'"/>
                    </div>
                    <div class="flex items-center">
                        <ButtonDefault
                            :btnLink="'/contact'"
                            :btnClass="'btn-sm btn btn-hover-primary btn-outline-black'"
                            :btnText="'Schedule a visit'"
                            :btnClassParent="'flex'"
                            class="hidden sm:inline-flex"
                        />

                    </div>
                </div>
                <div class="border-class flex w-full h-[1px] bg-white border-b-1 border-bordercolor"></div>
            </div>
        </div>
        <!-- Header Section End -->

        <OffcanvasSidebar :class="{'show-mobile-menu' : navOpen}" @togglenav="navOpen = !navOpen" />

        <!-- Breadcrumb Section Start -->
        <BreadcrumbSection :BreadcrumbSubTitle="'Service'" :BreadcrumbTitle="'Service'"/>
        <!-- Breadcrumb Section End -->

        <!-- Features Section Start -->
        <div class="section-padding pt-0">
            <div class="container-fluid">
                <Features/>
            </div>
        </div>
        <!-- Features Section End -->

        <!-- Activities Section Start -->
        <div class="border-b-1 border-bordercolor relative">
            <div class="bg-shape absolute -z-10 right-0 bottom-0 max-w-[50%]"><img src="/images/shapes/activities.png" alt="activities bg shape"></div>
            <div class="container-fluid">
                <div class="section-padding pt-0">
                    <SectionTitle
                        secTionMargin="mb-10"
                        subTitle="Activities in Ecostate"
                        title="a"
                        titleClass="hidden"
                    />
                    <ActivitiesSection/>
                </div>
            </div>
        </div>
        <!-- Activities Section End -->

        <!-- Footer Section Start -->
        <FooterSection/>
        <!-- Footer Section End -->

    </div>
</template>

<script>
export default {
    components: {
        LogoDark: () => import('@/components/logo/LogoDark'),
        MainMenu: () => import('@/components/header/MainMenu'),
        ButtonDefault: () => import('@/components/button/ButtonDefault'),
        BreadcrumbSection: () => import('@/components/BreadcrumbSection'),
        SectionTitle: () => import('@/components/title/SectionTitle'),
        Features: () => import('@/components/Features'),
        ActivitiesSection: () => import('@/components/ActivitiesSection')
    },
    data () {
        return {
            isSticky: false,
            navOpen: false
        }
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
    },
    mounted(){
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY
            if(scrollPos >= 100){
                this.isSticky = true
            } else {
                this.isSticky = false
            }
        })
    }
}
</script>
<style lang='scss' scoped>
.is-sticky {
    @apply bg-white transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;

    & .border-class {
        @apply hidden;
    }
}
</style>