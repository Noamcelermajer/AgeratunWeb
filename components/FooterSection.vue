<template>
    <div class="container-fluid">
        <div class="footer-top section-padding border-b-1 border-bordercolor">
            <div class="flex gap-y-8 flex-wrap">
                <div class="lg:w-1/3 sm:w-1/2 w-full">
                    <LogoDark class="max-w-[180px]" logLink="/"/>
                </div>
                <div class="footer-widget sm:w-1/2 lg:w-1/3 w-full">
                    <h4 class="footer-widget-title d-lg-none">Contact Us</h4>
                    <ul class="footer-widget-list">
                        <li class="text-[15px] mb-[14px] last:mb-0">223 Thatcher Road St, Brookly, Manhattan, <br>NY 10463, United States</li>
                        <li class="text-[15px] mb-[14px] last:mb-0"><a class="hover:text-primary transition-all duration-500" href="tel:03156898998">+031 5689 89 98</a></li>
                        <li class="text-[15px] mb-[14px] last:mb-0"><a class="hover:text-primary transition-all duration-500" href="mailto:contact@example.com">contact@example.com</a></li>
                    </ul>
                </div>
                <div class="footer-widget flex justify-between items-start sm:flex-row flex-col sm:gap-y-0 gap-y-8 w-full lg:w-1/3">
                    <div class="footer-widget-list sm:w-1/2 w-full">
                        <h4 class="footer-widget-title d-lg-none">Quick Links</h4>
                        <ul class="">
                            <li class="mb-[14px] last:mb-0"><n-link class="hover:text-primary transition-all duration-300 text-[15px]" to="/about">About Us</n-link></li>
                            <li class="mb-[14px] last:mb-0"><n-link class="hover:text-primary transition-all duration-300 text-[15px]" to="/contact">Contact</n-link></li>
                            <li class="mb-[14px] last:mb-0"><n-link class="hover:text-primary transition-all duration-300 text-[15px]" to="/service">Ecostates Service</n-link></li>
                            <li class="mb-[14px] last:mb-0"><n-link class="hover:text-primary transition-all duration-300 text-[15px]" to="/gallery">Gallery</n-link></li>
                            <li class="mb-[14px] last:mb-0"><n-link class="hover:text-primary transition-all duration-300 text-[15px]" to="/team/kate-ethelyn">Team Details</n-link></li>
                        </ul>
                    </div>
                    <div class="footer-social sm:w-1/2 w-full">
                        <h4 class="footer-widget-title d-lg-none">Follow Us On</h4>
                        <div class="social flex gap-2">
                            <a href="" class="relative flex items-center justify-center w-[45px] h-[45px] rounded-full hover:bg-primary hover:text-white transition-all duration-300 bg-[#f3f3f9]"><i class="text-[14px] fa fa-instagram"></i></a>
                            <a href="https://www.instagram.com/ageratun" class="relative flex items-center justify-center w-[45px] h-[45px] rounded-full hover:bg-primary hover:text-white transition-all duration-300 bg-[#f3f3f9]"><i class="text-[14px] fa fa-facebook"></i></a>
                            <a href="#" class="relative flex items-center justify-center w-[45px] h-[45px] rounded-full hover:bg-primary hover:text-white transition-all duration-300 bg-[#f3f3f9]"><i class="text-[14px] fa fa-twitter"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom py-10 lg:py-[50px] flex justify-between sm:flex-row flex-col-reverse items-center gap-y-2">
            <p class="footer-copyright text-center text-[15px]">© 2023 <a class="text-black" href="https://themeforest.net/user/bootxperts">Ageratun</a>. All Rights Reserved </p>
            <ul class="footer-language flex gap-7">
                <li class="text-[11px] uppercase"><a href="#">Eng</a></li>
                <li class="text-[11px] uppercase"><a href="#">rus</a></li>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    components: {
        LogoDark: () => import('@/components/logo/LogoDark')
    }
}
</script>
<style lang="scss" scoped>
.footer-widget-title {
    @apply lg:hidden block text-xl mb-5;
}
</style>