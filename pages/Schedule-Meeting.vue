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
        <!-- Breadcrumb Section Start -->
        <BreadcrumbSection :BreadcrumbSubTitle="'Contact us'" :BreadcrumbTitle="'Contact'"/>
        <!-- Breadcrumb Section End -->

         <!-- Contact Address and Location Section Start -->
    <div class="container-fluid">
        <div class="section-padding pt-0">
          <div class="centered">
            <h2 class="content-block-title">Subscribe for Project Information</h2>
            <ul class="feature-list flex flex-wrap flex-col md:flex-row mb-10 md:mb-16">
              <li v-for="(item, imageIndex) in items" :key="imageIndex" class="text-lg pb-6 last:pb-0 relative table md:w-1/2 pl-10 text-black last:mb-0 before:content-['\f12d'] before:font-[flaticon] before:text-xs before:absolute before:top-0 md:before:top-1 before:left-0 before:w-6 h-6 before:text-center before:text-white before:rounded-full before:bg-primary before:leading-[24px]">{{item.title}}</li>
            </ul>
            <form id="contact-form" class="grid gap-x-10 grid-cols-2" action="https://getform.io/f/6af30b8c-e767-4d30-b964-d7e38d35078b" method="POST">
              <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                <input type="text" class="text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Name">
              </div>
              <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                <input type="text" class=" text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Phone">
              </div>
              <div class="single-fild col-span-2 mb-5">
                <input type="email" class=" text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="E-mail">
              </div>
              <div class="single-fild col-span-2">
                <textarea class="h-32 mb-6 text-[15px] relative block w-full py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Write from here" spellcheck="false" data-gramm="false"></textarea>
                <div class="flex justify-start w-full md:mt-10">
                  <button type="submit" value="submit" name="submit" class="btn btn-md btn-light btn-hover-primary max-w-[150px] md:max-w-[200px] w-full">Submit</button>
                  <p class="form-messege"></p>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      <!-- Contact Address and Location Section End -->
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
.centered {
    @apply flex justify-center items-center min-h-screen bg-gray-100;
  }
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