<template>
    <div class="container-fluid">
        <div class="section-padding">
            <div class="flex lg:flex-row flex-col gap-10">
                <div class="lg:w-1/2 w-full flex-auto">
                    <div class="relative mr-0 xl:mr-[35px] 2xl:pr-[190px] xl:pr-[100px] lg:pr-0 md:pr-[190px] pr-0 lg:pb-[100px] xl:pb-[130px] md:pb-[130px] pb-[70px]">
                        <img class="2xl:w-auto w-[85%] md:w-auto lg:w-[85%] xl:w-[87%]" src="/images/about/about-1.jpg" alt="About-Image">
                        <img class="absolute z-20 right-0 bottom-0 w-[85%] md:w-auto lg:w-[85%] xl:w-[80%] 2xl:w-auto" src="/images/about/about-2.jpg" alt="About-Image">
                    </div>
                </div>
                <div class="lg:w-1/2 w-full flex-auto">
                    <div class="about-content 2xl:pl-8">
                        <!-- Section Title Start -->
                        <SectionTitle
                            secTionMargin="2xl:pb-[85px] xl:pb-[70px] lg:pb-[60px] pb-[20px]"
                            subTitle="Thessaloniki"
                            title="Sky Tower Project"
                            titleClass="lg:mt-10 mt-5 font-play text-[26px] sm:text-[36px] md:text-[44px] lg:text-[50px] xl:text-[54px] 2xl:text-7xl font-normal uppercase text-white"
                        />
                        <!-- Section Title End -->
                        <p class="text-light opacity-[0.75] mb-4">The Sky Tower has 8 floors and underground parking. You've got luxury apartments, modern studios, and two-room flats, all fully furnished. Each has a balcony with views of the sea and city.</p>
                        <p class="text-light opacity-[0.75]">On the eighth floor, there's an infinity pool that overlooks the sea. Right next to it, you'll find a bar and restaurant with indoor and outdoor seating.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    components: {
        SectionTitle: () => import('@/components/title/SectionTitle')
    }
}
</script>

<style>

</style>