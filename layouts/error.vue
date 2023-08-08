<template>
    <div>

        <!-- Header Section Start -->
        <div class="relative top-0 left-0 right-0 z-[999]">
            <div class="container-fluid mx-auto">
                <div class="flex justify-between items-center">
                    <div class="flex items-center">
                        <LogoDark class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/home"/>
                        <MainMenu :textClass="'text-black'"/>
                    </div>
                    <div class="flex items-center">
                        <ButtonDefault
                            :btnLink="'/'"
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
                <div class="flex w-full h-[1px] bg-white border-b-1 border-bordercolor"></div>
            </div>
        </div>
        <!-- Header Section End -->

        <!-- Offcanvas Section Start -->
        <OffcanvasSidebar :class="{'show-mobile-menu' : navOpen}" @togglenav="navOpen = !navOpen" />
        <!-- Offcanvas Section End -->

        <!-- Error Section Start -->
        <div class="border-b-1 border-bordercolor">
            <div class="container-fluid">
                <div class="section-padding">
                    <div class="max-w-[650px] mx-auto text-center">
                        <h2 class="sm:text-[200px] text-[120px] leading-[1] mb-2">404</h2>
                        <p class="sm:text-[30px] text-[24px] font-semibold leading-[1.4] mb-[40px]">We’re unable to find a page you are looking for, Try later or click the button.</p>
                        <ButtonDefault
                            :btnLink="'/booking'"
                            :btnClass="'min-w-[200px] min-h-[50px] md:min-h-[60px] py-2 sm:py-5 btn text-center relative overflow-hidden h-[54px] lg:h-[60px] px-[30px] lg:px-[40px] text-[14px] flex items-center justify-center btn-primary btn-hover-dark'"
                            :btnText="'Back to Home'"
                            :btnClassParent="'flex text-center justify-center leading-[1]'"
                        />
                    </div>
                </div>
            </div>
        </div>
        <!-- Error Section End -->

        <!-- Footer Section Start -->
        <FooterSection/>
        <!-- Footer Section End -->

    </div>
</template>

<script>
    export default {
        props: ['error'],
        layout: 'error' ,
        components: {
            LogoDark: () => import('@/components/logo/LogoDark'),
            MainMenu: () => import('@/components/header/MainMenu'),
            ButtonDefault: () => import('@/components/button/ButtonDefault'),
            BreadcrumbSection: () => import('@/components/BreadcrumbSection'),
            SectionTitle: () => import('@/components/title/SectionTitle')
        },
        data () {
            return {
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
        }
    }
</script>
<style lang='scss'>

</style>