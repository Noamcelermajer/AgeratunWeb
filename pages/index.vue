<template>
    <div>
      <!-- Header Section Start -->
      <div class="absolute top-0 left-0 right-0 z-[999]" :class="{'is-sticky': isSticky}">
        <div class="container-fluid mx-auto">
          <div class="flex justify-between items-center">
            <div class="flex items-center" >
              <Logo v-if="!isSticky" class="sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/"/>
              <LogoDark v-else class="relative z-50 sm:max-w-[180px] max-w-[150px] mr-20 2xl:mr-[180px] py-[20px]" logLink="/"/>
            </div>
            <div class="flex items-center">
                <ButtonDefault 
                    @click="scrollToSection"
                    :btnClass="'btn-sm btn btn-hover-primary btn-outline-light'"
                    :btnText="'Schedule a visit'"
                    :btnClassParent="'flex'"
                    class="hidden sm:inline-flex"
                /> 

                    </div>
                </div>
            </div>
        </div>
        <!-- Header Section End -->
        <!-- Hero Slider Section Start -->
        <div class="relative">
            <HeroTwo />
        </div>
        <!-- Hero Slider Section End -->

        <!-- Funfact Section Start -->
        <div class="bg-themedark">
            <FunfactTwo/>
        </div>
        <!-- Funfact Section End -->
        <div class="bg-themedark relative before:content-[''] before:absolute before:top-full before:left-0 before:w-full before:h-[50px] md:before:h-[70px] lg:before:h-[133px] mb-[50px] md:mb-[70px] lg:mb-[133px] before:bg-no-repeat before:bg-center before:bg-cover before:bg-[url('/images/shapes/about.png')]">
          <AboutHometwo />
      </div>
        <div class="container-fluid">
            <div class="section-padding">
              <h3 class="font-bold text-2xl mb-4 text-center">Project Overview</h3>
              <p class="text-lg mb-8">
                "Sky Tower" is a luxurious real estate project situated along Thessaloniki's picturesque seafront. This exclusive development offers an exceptional vacation experience.
              </p>
              <p class="text-lg mb-8">
                The project spans the first line of the sea and comprises a collection of meticulously designed and exquisitely furnished apartments, each boasting breathtaking views. The architectural style combines contemporary elegance with elements inspired by the surrounding beach environment, creating a harmonious and captivating atmosphere.
              </p>
              <p class="text-lg mb-8">
                Within the property, a meticulously landscaped lush garden provides a serene oasis, offering residents a refuge from the bustling city. With carefully crafted greenery, elegant pathways, and tranquil seating areas, the garden provides an ideal environment for relaxation, contemplation, or social gatherings.
              </p>
              <p class="text-lg mb-8">
                On the rooftop, a restaurant presents gourmet cuisine and panoramic views of Thessaloniki's skyline. Residents can savor delightful meals prepared by renowned chefs while enjoying a wide selection of wines, all in an enchanting setting high above the city.
              </p>
              <p class="text-lg mb-8">
                The prime beachfront location, unrivaled amenities including a swimming pool, fitness center, garden, and rooftop restaurant, along with a focus on delivering exceptional living experiences to discerning residents, make "Sky Tower" the epitome of luxury living in Thessaloniki, offering unparalleled vacation residences.
              </p>
            </div>
        <!-- Highlight Section Start -->
        <div class="w-full">
            <div class="container-fluid">
                <div class="section-padding">

                    <!-- Section Title Start -->
                    <SectionTitle
                        secTionMargin="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center"
                        subTitle="Highlight"
                        title="Sky Tower's Facilities"
                        titleClass="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase"
                    />
                    <!-- Section Title End -->

                    <HighlightSection/>
                    
                </div>
            </div>
        </div>
        <!-- Highlight Section End -->

        </div>
        <!-- Floor Plan Section Start -->
        <div class="bg-[#f5f1ef]" id="floor-plans">
            <div class="container-fluid">
                <div class="section-padding pb-[60px] lg:pb-[100px]">
                    <!-- Section Title Start -->
                    <SectionTitle
                        secTionMargin="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center"
                        subTitle="Apartment Plan"
                        title="Apartment Plans"
                        titleClass="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase"
                    />
                    <!-- Section Title End -->
                    <TabStyleTwo @scroll-to-section="scrollToSection"/>
                </div>
            </div>
        </div>
        <!-- Floor Plan Section End -->

        <!-- Gallery Section Start -->
        <div class="container-fluid">
            <div class="section-padding border-b-1 border-bordercolor">
                <!-- Section Title Start -->
                <SectionTitle
                    secTionMargin="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center"
                    subTitle="Photos and Videos"
                    title="Sky Tower Album"
                    titleClass="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase"
                />
                <!-- Section Title End -->
                <GallerySliderMain/>
            </div>
        </div>
        <!-- Gallery Section End -->


        <!-- Location State Section Start -->
        <div class="bg-themedark relative before:content-[''] before:absolute before:bottom-full before:left-0 before:w-full before:h-[50px] md:before:h-[70px] lg:before:h-[133px] mt-[50px] md:mt-[70px] lg:mt-[133px] before:bg-no-repeat before:bg-center before:bg-cover ">
            <div class="container-fluid">
                <div class="section-padding pb-0">
                    <SectionTitle
                        secTionMargin="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[30px] text-center"
                        subTitle=""
                        title="Nearby Attraction"
                        titleClass="lg:mt-10 md:mt-[30px] mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase text-white"
                    />
                </div>
            </div>
            <LocationStateTwo/>
        </div>
        <!-- Location State Section End -->

        <!-- Home Two Contact Section Start -->
        <Contact ref="contact-section" />
        <!-- Home Two Contact Section End -->

        <!-- Footer Section Start -->
        <FooterSectionTwo/>
        <!-- Footer Section End -->

    </div>
</template>

<script>
import smoothScroll from 'vue2-smooth-scroll'

export default {
    components: {
        Logo: () => import('@/components/logo/Logo'),
        MainMenu: () => import('@/components/header/MainMenu'),
        ButtonDefault: () => import('@/components/button/ButtonDefault'),
        HeroTwo: () => import('@/components/HeroTwo'),
        FunfactTwo: () => import('@/components/FunfactTwo'),
        SectionTitle: () => import('@/components/title/SectionTitle'),
        HighlightSection: () => import('@/components/HighlightSection'),
        TabStyleTwo: () => import('@/components/TabStyleTwo'),
        GallerySliderMain: () => import('@/components/gallery/GallerySliderMain'),
        LocationStateTwo: () => import('@/components/LocationStateTwo'),
        HomeTwoContact: () => import('@/components/HomeTwoContact'),
        FooterSectionTwo: () => import('@/components/FooterSectionTwo'),
        LogoDark : () => import('@/components/logo/LogoDark.vue'),
        Contact : () => import ('@/components/Contact.vue')

    },
    data () {
    return {
      isSticky: false,
      navOpen: false
    }
  },
  methods: {
    scrollToSection() {
  let element = this.$refs['contact-section'].$el;
  let elementY = window.scrollY + element.getBoundingClientRect().top;
  let startingY = window.scrollY;
  let diff = elementY - startingY;
  let duration = 300; // Changed to 800ms for a more typical animation speed
  let start;

  const step = (timestamp) => {
    if (!start) start = timestamp;
    let time = timestamp - start;
    let percent = Math.min(time / duration, 1);
    
    window.scrollTo(0, startingY + diff * percent);
    
    if (time < duration) {
      window.requestAnimationFrame(step);
    }
  };

  window.requestAnimationFrame(step);
},
    mounted(){

      window.addEventListener('scroll', this.updateStickyState);
    },
    updated() {
    },
    beforeDestroy() {

      window.removeEventListener('scroll', this.updateStickyState);
    },
      updateStickyState() {
        let scrollPos = window.scrollY
        if(scrollPos >= 100){
          this.isSticky = true
        } else {
          this.isSticky = false
        }
      }
  }
} 

</script>
<style lang='scss' scoped>

.is-sticky {
    @apply bg-black transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;

    & .border-class {
        @apply hidden;
    }
}
</style>