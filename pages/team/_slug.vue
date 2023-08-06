<template>
    <div class="">

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
        <BreadcrumbSection :BreadcrumbSubTitle="'About Agent'" :BreadcrumbTitle="'About Agent'"/>
        <!-- Breadcrumb Section End -->

        <!-- Mainwrapper Start Here -->
        <div class="container-fluid">
            <div class="section-padding pt-0 border-b-1 border-bordercolor flex gap-10 lg:gap-6 lg:flex-row flex-col">
                <div class="lg:w-2/6 w-full">
                    <div class="bg-light p-10 max-w-[395px]">
                        <div class=" block overflow-hidden mb-6 bg-primary">
                            <img class="w-full" :src="teamData.image" alt="Blog">
                        </div>
                        <div class="">
                            <h3 class="text-[24px] mb-0">{{teamData.membername}}</h3>
                            <span class="text-[13px]">{{teamData.membersubtitle}}</span>
                            <ul class="mt-[18px]">
                                <li v-for="(info, index) in teamData.infoData" :key="index" class="text-[13px] xl:text-[15px]">
                                    <span class="text-black font-bold">{{info.infotext}}</span> <span>{{info.infonumber}}</span>
                                </li>
                            </ul>
                            <ul class="team-social flex gap-[18px] mt-4">
                                <li v-for="(social, index) in teamData.socialData" :key="index">
                                    <a class="text-[16px] text-[#999999]" :href="social.link" target="_blank"><i :class="social.icon"></i></a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="lg:w-2/3 w-full">
                    <div class="mb-12">
                        <h2 class="text-4xl mb-6">About {{teamData.membername}}</h2>
                        <p class="mb-3 lg:mb-4">Andy Robertson will take care of every detail in the sale of your property. He is readily available and very knowledgeable. He went above and beyond in vhelping sell my house. Nam congue nisi eu orci laoreet, nec tristique dolor scelerisque. Aenean mauris sem, commodo et accumsan ac, dictum vitae sem. Sed bibendum nunc neque, in auctor enim. Proin ornare nibh libero, id euismod nulla.</p>
                        <p>This 14+ acre site would make an ideal place for your new home with 926′ of road frontage. Well already in!! owner has survey wich shows a home and pond! Ideal development parcel, Endless possibilities to enjoy this land. easy access to US 23.A perfect place to build your dream home. Chose the home you want and the landscape. Bring your horses or llamas! close to shopping.</p>
                    </div>
                    <div class="mb-12">
                        <h3 class="text-2xl mb-5">Experiences</h3>
                        <p class="mb-5">10+ years experience with over 100+ apartments for sell and 80+ for rent</p>
                        <ul class="">
                            <li class="mb-2 relative pl-7 before:absolute before:top-[11px] before:left-0 before:w-[5px] before:h-[5px] before:content-[''] before:rounded-full before:bg-black" v-for="(item, index) in teamData.experienceData" :key="index">
                                <strong class="text-black">{{item.boldtext}}</strong> {{item.normaltext}}
                            </li>
                        </ul>
                    </div>
                    <div class="mb-12">
                        <h3 class="text-2xl mb-5">Area & Project</h3>
                        <ul class="">
                            <li class="mb-2 relative" v-for="(item, index) in teamData.areaData" :key="index">
                                <p>{{item.areatext}}</p>
                            </li>
                        </ul>
                    </div>
                    <div class="mb-12">
                        <h3 class="text-2xl mb-5">Property Type</h3>
                        <ul class="flex flex-wrap gap-1">
                            <li class="mb-2 relative" v-for="(item, index) in teamData.propertyData" :key="index">
                                <n-link to="/">{{item.propertytext}},</n-link>
                            </li>
                        </ul>
                    </div>
                    <div class="mb-12">
                        <h3 class="text-2xl mb-5">Contact</h3>
                        <p class="mb-5">Required fileds are marked *</p>
                        <form id="contact-form" 
                            class="grid gap-x-10 grid-cols-2" 
                            action="https://getform.io/f/6af30b8c-e767-4d30-b964-d7e38d35078b" 
                            method="POST">
                            <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                                <input type="text" class="text-[15px] relative block w-full h-[60px] py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="First Name">
                            </div>
                            <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                                <input type="text" class="text-[15px] relative block w-full h-[60px] py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Last Name">
                            </div>
                            <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                                <input type="email" class=" text-[15px] relative block w-full h-[60px] py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="E-mail">
                            </div>
                            <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                                <input type="text" class=" text-[15px] relative block w-full h-[60px] py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Phone">
                            </div>
                            <div class="single-fild col-span-2">
                                <textarea class="h-32 mb-6 text-[15px] relative block w-full py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Write from here" spellcheck="false" data-gramm="false"></textarea>
                                <div class="flex justify-start w-full md:mt-10">
                                    <button type="submit" value="submit" name="submit" class="btn btn-md btn-outline-black btn-hover-primary max-w-[180px] md:max-w-[220px] w-full">Submit Now</button>
                                    <p class="form-messege"></p>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <!-- Mainwrapper End Here -->

        <!-- Footer Section Start -->
        <FooterSection/>
        <!-- Footer Section End -->

    </div>
</template>

<script>
    import teamData from '@/data/teamdata.json'
    export default {
        components: {
            LogoDark: () => import('@/components/logo/LogoDark'),
            MainMenu: () => import('@/components/header/MainMenu'),
            ButtonDefault: () => import('@/components/button/ButtonDefault'),
            BreadcrumbSection: () => import('@/components/BreadcrumbSection'),
            GallerySquare: () => import('@/components/gallery/GallerySquare'),
            SectionTitle: () => import('@/components/title/SectionTitle')
        },
        data() {
            return {
                isSticky: false,
                teamData,
                navOpen: false,
                slug: this.$route.params.slug
            }
        },
        mounted () {
            this.teamData = teamData.find(member => this.slugify(member.membername) == this.$route.params.slug);
            
            window.addEventListener('scroll', () => {
                let scrollPos = window.scrollY
                if(scrollPos >= 100){
                    this.isSticky = true
                } else {
                    this.isSticky = false
                }
            })
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
            slugify(text) {
                return text
                .toString()
                .toLowerCase()
                .replace(/\s+/g, "-") // Replace spaces with -
                .replace(/[^\w-]+/g, "") // Remove all non-word chars
                .replace(/--+/g, "-") // Replace multiple - with single -
                .replace(/^-+/, "") // Trim - from start of text
                .replace(/-+$/, ""); // Trim - from end of text
            }
        }
    }
</script>

<style lang="scss" scoped>
.btn {
    @apply z-20 before:content-[""] before:absolute before:right-0 before:top-0 before:w-[200%] before:h-[200%] before:transition-all before:duration-700 before:-z-10 before:rounded-[0%] uppercase before:opacity-0 hover:before:opacity-100;
}
.btn-md {
    @apply text-dark h-[60px] px-[30px] py-[15px] text-[14px] leading-[1] relative inline-block overflow-hidden items-center transition-all duration-700;
}
.btn-hover-primary {
    @apply hover:border-[#0EA478] hover:text-white before:bg-[#0EA478] hover:transition-all hover:duration-700;
}
.btn-outline-black {
    @apply bg-white border-1 border-black;
}
.is-sticky {
    @apply bg-white transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;

    & .border-class {
        @apply hidden;
    }
}
</style>