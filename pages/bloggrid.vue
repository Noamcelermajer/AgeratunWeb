<template>
    <div>

        <!-- Header Section Start -->
        <div class="relative top-0 left-0 right-0 z-[999]" :class="{'is-sticky': isSticky}">
            <div class="container-fluid mx-auto">
                <div class="flex justify-between items-center">
                    <div class="flex items-center">
                        <LogoDark class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/home"/>
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
                        <!-- Offcanvas Button Start -->
                        <div class="lg:hidden block leading-[1rem] ml-[10px] sm:ml-[15px]">
                            <button class="overflow-hidden bg-transparent h-[18px] relative w-[26px]" @click="mobiletoggleClass('addClass', 'show-mobile-menu')">
                                <span class="w-full h-[2px] bg-black block my-2 transition-all before:content-[''] before:top-0 before:bottom-auto before:absolute before:left-0 before:w-full before:h-[2px] before:bg-black after:content-[''] after:absolute after:left-0 after:w-full after:h-[2px] after:bg-black after:top-auto after:bottom-0"></span>
                            </button>
                        </div>
                        <!-- Offcanvas Button End --> 
                    </div>
                </div>
                <div class="border-class flex w-full h-[1px] bg-white border-b-1 border-bordercolor"></div>
            </div>
        </div>
        <!-- Header Section End -->

        <!-- Offcanvas Section Start -->
        <OffcanvasSidebar :class="{'show-mobile-menu' : navOpen}" @togglenav="navOpen = !navOpen" />
        <!-- Offcanvas Section End -->

        <!-- Breadcrumb Section Start -->
        <BreadcrumbSection :borderClass="'flex justify-center text-center'" :centerClass="'justify-center'" :BreadcrumbSubTitle="'Blog'" :BreadcrumbTitle="'Ecostate’s Magazine'"/>
        <!-- Breadcrumb Section End -->

        <!-- Blog Section Start -->
        <div class="border-b-1 border-bordercolor">
            <div class="container-fluid">
                <div class="section-padding pt-0">
                    <div class="flex gap-12 lg:gap-8 lg:flex-row flex-col">
                        <BlogGrid />
                    </div>
                </div>
            </div>
        </div>
        <!-- Blog Section End -->

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
            OffcanvasSidebar: () => import('@/components/header/OffcanvasSidebar'),
            ButtonDefault: () => import('@/components/button/ButtonDefault'),
            BreadcrumbSection: () => import('@/components/BreadcrumbSection'),
            BlogGrid: () => import('@/components/BlogGrid'),
            SectionTitle: () => import('@/components/title/SectionTitle')
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