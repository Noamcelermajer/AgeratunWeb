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

        <OffcanvasSidebar :class="{'show-mobile-menu' : navOpen}" @togglenav="navOpen = !navOpen" />

        <!-- Breadcrumb Section Start -->
        <BreadcrumbSection :BreadcrumbSubTitle="'Contact us'" :BreadcrumbTitle="'Contact'"/>
        <!-- Breadcrumb Section End -->

        <!-- Contact Address and Location Section Start -->
        <div class="container-fluid">
            <div class="section-padding pt-0">
                <div class="flex justify-between gap-y-10 lg:flex-row flex-col">
                    <div class="lg:w-5/12 w-full">
                        <div class="">
                            <div class="mb-12">
                                <h3 class="lg:text-[36px] md:text-[30px] sm:text-[26px] text-[24px] leading-[1.277] mb-6">Representative Office</h3>
                                <ul>
                                    <li class="mb-[14px]">223 Thatcher Road St, Brookly, Manhattan, NY 10463, United States</li>
                                    <li class="mb-[14px]"><a href="tel:+03156898998">+031 5689 89 98</a></li>
                                    <li class="mb-[14px]"><a href="mailto:contact@example.com">contact@example.com</a></li>
                                </ul>
                            </div>
                            <div class="mb-12">
                                <h3 class="lg:text-[36px] md:text-[30px] sm:text-[26px] text-[24px] leading-[1.277] mb-6">Representative Office</h3>
                                <ul>
                                    <li class="mb-[14px]"><a href="tel:+03156082612">+031 5608 26 12</a></li>
                                    <li class="mb-[14px]"><a href="mailto:business@example.com">business@example.com</a></li>
                                </ul>
                            </div>
                            <div>
                                <h3 class="lg:text-[36px] md:text-[30px] sm:text-[26px] text-[24px] leading-[1.277] mb-6">Customer Care</h3>
                                <ul>
                                    <li class="mb-[14px]"><a href="tel:+03132417152">+031 3241 71 52</a></li>
                                    <li class="mb-[14px]"><a href="mailto:customer@example.com">customer@example.com</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="lg:w-7/12 w-full">
                        <div class="pl-0">
                            <div class="map-location-layer">
                                <img src="/images/locations/map-1.png" loading="lazy" alt="location map" width="845" height="672">
                                <div :style="state.style" v-for="(state, index) in location" :key="index" :id="state.id" class="map-location-item" :class="[index === active ? 'active' : '']" @click='activate(index)'>
                                    <span class="title">{{state.name}}</span>
                                </div>
                                <a class="google-map-link" href="https://www.google.com/maps/@23.1866368,89.6499712,13z" target="_blank"><i class="fi fi-map-1 mr-2"></i>OPEN GOOGLE MAP</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Contact Address and Location Section End -->

        <!-- Agent Section Start -->
        <div class="bg-light">
            <div class="container-fluid">
                <div class="section-padding">
                    <AgentSection/>
                </div>
            </div>
        </div>
        <!-- Agent Section End -->

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
            AgentSection: () => import('@/components/AgentSection'),
            SectionTitle: () => import('@/components/title/SectionTitle')
        },
        data () {
            return {
                isSticky: false,
                navOpen: false,
                active: 0,
                location: [
                    {
                        id: "map-location-1",
                        name: "Gaucho Restaurant",
                        style: "top: 20%; left: 35%"
                    },
                    {
                        id: "map-location-2",
                        name: "Manhattan Hospital",
                        style: "left: 18%; top: 45%"
                    },
                    {
                        id: "map-location-3",
                        name: "Costco Supermarket Center",
                        style: "left: 28%; bottom: 25%"
                    },
                    {
                        id: "map-location-4",
                        name: "Ecostate Park",
                        style: "left: 48%; top: 25%"
                    },
                    {
                        id: "map-location-5",
                        name: "Harvard University",
                        style: "right: 31%; bottom: 39%"
                    }
                ]
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
            },
                        
            activate(index) {
                this.active = index;
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
.map-location-layer{
    @apply relative -mt-0 2xl:-mt-[120px];
}
.map-location-item{

    @apply absolute w-[10px] h-[10px] cursor-pointer rounded-full bg-primary shadow-[0_0_0_10px_rgba(14,164,120,0.1)];

    & .title {
        @apply opacity-0 invisible text-sm whitespace-nowrap font-semibold absolute -top-[70px] left-1/2 transform -translate-x-1/2 text-black py-1 px-4 transition-all duration-500 rounded-[4px] bg-white shadow-[0_10px_40px_0_rgba(0,0,0,0.15)] before:absolute before:-bottom-6 before:left-1/2 before:w-[10px] before:h-6 before:transform before:-translate-x-1/2 before:bg-white before:content-[''];

        &::before {
            clip-path: polygon(0% 0%, 100% 0%, 50% 100%, 50% 100%, 0% 0%);
        }
    }
    &.active {
        & .title {
            @apply opacity-100 visible duration-500 transition-all
        }
    }
}
.google-map-link {
    @apply absolute bottom-0 left-0 w-full text-center text-[#064DF0];
}
.is-sticky {
    @apply bg-white transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;

    & .border-class {
        @apply hidden;
    }
}
</style>