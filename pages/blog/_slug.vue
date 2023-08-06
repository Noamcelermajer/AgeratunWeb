<template>
    <div class="relative">

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

                    </div>
                </div>
                <div class="border-class flex w-full h-[1px] bg-white border-b-1 border-bordercolor"></div>
            </div>
        </div>
        <!-- Header Section End -->


        <!-- Breadcrumb Section Start -->
        <div class="container-fluid">
            <div class="breadcrumb lg:py-[100px] md:py-[80px] py-[60px]">
                <div class="breadcrumb_banner text-left">
                    <ul class="breadcrumb_meta flex items-center justify-center gap-5 mb-3 md:mb-5 lg:mb-8">
                        <li class="relative"><n-link class="relative before:absolute before:content-['/'] before:-top-[3px] before:-right-3" to="/">Home</n-link></li>
                        <li class="relative"><n-link class="relative before:absolute before:content-['/'] before:-top-[3px] before:-right-3" to="/bloggrid">Blog</n-link></li>
                        <li class="relative"><span class="relative text-black">Blog Details</span></li>
                    </ul>
                    <h2 class="md:text-[60px] sm:text-[40px] text-[30px] font-bold text-black mb-0 relative text-center leading-[1.167] block">{{blogData.title}}</h2>
                </div>
            </div>
        </div>
        <!-- Breadcrumb Section End -->

        <!-- Mainwrapper Start Here -->
        <div class="w-full h-full border-b-1 border-bordercolor">

            <section class="section w-full flex justify-center items-center pb-20 lg:pb-[120px] dark:bg-[#3b3b3b]">
                <div class="">
                    <div class="container-fluid lg:mb-[70px] mb-12">
                        <img class="w-full" :src="blogData.bigimage" alt="Blog">
                    </div>
                    <div class="sm:px-[30px] px-4 w-full lg:w-5/6 xl:w-7/12 mx-auto">
                        <div class="flex md:justify-between md:flex-row flex-col items-center mt-6 mb-12 pb-6 border-b-1 border-bordercolor gap-5 md:gap-7 lg:gap-10">
                            <ul class="meta-top flex items-center gap-3">
                                <li class="flex gap-3 after:content-[''] after:bg-[#cccccc] after:h-4 after:w-[1px] after:right-0 after:top-0 after:self-center">
                                    <span class="text-black text-sm font-normal uppercase relative hover:text-primary transition-all">{{blogData.category}}</span>
                                </li>
                                <li class="text-sm">{{blogData.date}}</li>
                            </ul>
                            <ul class="blog-meta flex flex-wrap gap-7">
                                <li class="text-sm flex gap-1">
                                    <i class="text-[24px] leading-[1] flex self-center fi fi-user"></i>By
                                    <span class="text-black hover:text-primary transition-all">Ecostateusar</span>
                                </li>
                                <li class="text-sm flex gap-1">
                                    <i class="text-[24px] leading-[1] flex self-center fi fi-pulse-rate"></i>155 Views
                                </li>
                            </ul>
                        </div>
                        <h3 class="lg:text-[26px] text-[20px] font-bold mb-7 text-black mt-10 leading-[1.5]">Three legendary “<span class="text-primary">big men</span>” of US with hundreds of years of history have joined hands with EcoGroup Cor to develop Ecostate Park therapeutic twin towers.</h3>
                        <p class="mb-7">The problem is that when you do use your brakes, you actually wear them away ever so slightly every time. The various parts in your brake system come together to bring each wheel to a halt as efficiently as possible, and it is this coming together that actually compromises the performance of your brakes.</p>
                        <p class="mb-7">It is important to add here that you should not stop using your car brakes, but you should be checking their condition on a regular basis</p>
                        <div class="grid md:grid-cols-2 grid-cols-1 gap-7 mb-7">
                            <img class="w-full" src="/images/blog/blog-single-2-1.jpg" alt="Image">
                            <img class="w-full" src="/images/blog/blog-single-2-2.jpg" alt="Image">
                        </div>
                        <p><strong class="text-black">The short answer is yes</strong>. According to Kross, when you think of yourself as another person, it allows you give yourself more objective, helpful feedback.</p>
                        <blockquote class="relative block my-12 p-5 sm:p-10 md:p-[60px] border-1 border-bordercolor bg-light">
                            <div class="quote-icon absolute top-5 sm:top-10 md:top-14 right-5 sm:right-10 md:right-14">
                                <img src="/images/icons/quote-1.png" alt="quote icon">
                            </div>
                            <span class="meta text-base font-semibold block max-w-[70%] text-black mb-6 md:mb-8">James Howlet - <span class="text-sm font-normal">Strategy Investor at Amazon Invest</span></span>
                            <p class="md:text-[24px] text-[20px] leading-[1.5] text-black">“Ecostate certainly will become the most of residentials worthy and super profit in Mahantan in 2024”</p>
                        </blockquote>
                        <h3 class="mb-8 text-[26px] leading-[1.5]">3 Reasons to investing at this moment</h3>
                        <p class="mb-7">The first, and most obvious, is a noise when you apply the brake pedal. This could be anything from a grinding sound to a high-pitched screech, and may be indicative that the brake pads are wearing thin and the calipers</p>
                        <ul class="my-10 pl-8">
                            <li class="relative text-base pl-7 mt-3 first:mt-0 before:absolute before:top-[10px] before:left-0 before:w-[5px] before:h-[5px] before:content-[''] before:rounded-full before:bg-[#666666]">Welsh novelist Sarah Waters sums it up eloquently</li>
                            <li class="relative text-base pl-7 mt-3 first:mt-0 before:absolute before:top-[10px] before:left-0 before:w-[5px] before:h-[5px] before:content-[''] before:rounded-full before:bg-[#666666]">In their classic book, Creativity in Business, based on a popular course tvhey co-taught</li>
                            <li class="relative text-base pl-7 mt-3 first:mt-0 before:absolute before:top-[10px] before:left-0 before:w-[5px] before:h-[5px] before:content-[''] before:rounded-full before:bg-[#666666]">Novelist and screenwriter Steven Pressfield</li>
                        </ul>
                        <p class="mb-7">That immediately brought to mind one of my fondest memories, involving my daughter when she was just a toddler of one.</p>
                        <div class="flex pt-10 border-t-1 border-bordercolor mb-10">
                            <span class="text-black mr-5">Share:</span>
                            <div class="social flex gap-5">
                                <a href="#" class="relative hover:text-primary transition-all duration-300 text-dark"><i class="text-[14px] fa fa-instagram"></i></a>
                                <a href="#" class="relative hover:text-primary transition-all duration-300 text-dark"><i class="text-[14px] fa fa-facebook"></i></a>
                                <a href="#" class="relative hover:text-primary transition-all duration-300 text-dark"><i class="text-[14px] fa fa-twitter"></i></a>
                                <a href="#" class="relative hover:text-primary transition-all duration-300 text-dark"><i class="text-[14px] fa fa-pinterest"></i></a>
                            </div>
                        </div>
                        <h3 class="mb-5 text-[26px] leading-[1.5]">Comments</h3>
                        <!-- Blog Details Comment Start -->
                        <Disqus shortname='Admin' />
                        <!-- Blog Details Comment End -->
                    </div>
                </div>
            </section>

        </div>
        <!-- Mainwrapper End Here -->

        <!-- Footer Section Start -->
        <FooterSection />
        <!-- Footer Section End -->
        
    </div>
</template>

<script>
    import blogData from '@/data/blogdata.json'
    import { Disqus } from 'vue-disqus'
    export default {
        components: {
            LogoDark: () => import('@/components/logo/LogoDark'),
            MainMenu: () => import('@/components/header/MainMenu'),
            ButtonDefault: () => import('@/components/button/ButtonDefault'),
            SectionTitle: () => import('@/components/title/SectionTitle'),
            FooterSection: () => import('@/components/FooterSection'),
            Disqus
        },
        data() {
            return {
                isSticky: false,
                blogData,
                navOpen: false,
                slug: this.$route.params.slug
            }
        },
        mounted () {
            this.blogData = blogData.find(blog => this.slugify(blog.title) == this.$route.params.slug);
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
.is-sticky {
    @apply bg-white transition-all shadow-[2px_4px_8px_rgba(52,58,64,0.15)] fixed z-9999;

    & .border-class {
        @apply hidden;
    }
}
</style>