<template>
    <div class="sidebar">
        <!-- Sidebar Widget Start -->
        <div class="sidebar_widget">
            <form action="#" class="sidebar_widget__search">
                <input type="text" placeholder="Search" class="sidebar_widget__search__input">
                <button class="sidebar_widget__search__btn">
                    <i class="fa fa-search"></i>
                </button>
            </form>
        </div>
        <!-- Sidebar Widget End -->

        <!-- Sidebar Widget Start -->
        <div class="sidebar_widget">
            <h3 class="sidebar_widget__title">Recent Post</h3>
            <div class="sidebar_widget__link">
                <div class="sidebar_widget__post" v-for="(blog, imageIndex) in blogData.slice(0, 3)" :key="imageIndex">
                    <div class="sidebar_widget__post__thumb">
                        <n-link class="overflow-hidden" :to="`/blog/${slugify(blog.title)}`"><img :src="blog.sidebarimage" alt="Post"></n-link>
                    </div>
                    <div class="sidebar_widget__post__content">
                        <ul class="blog-meta flex">
                            <li class="text-sm flex gap-1">
                                <i class="text-[24px] leading-[1] flex fi fi-user"></i>By <n-link class="text-black hover:text-primary transition-all" :to="`/blog/${slugify(blog.title)}`">Ecostateusar</n-link>
                            </li>
                        </ul>
                        <n-link :to="`/blog/${slugify(blog.title)}`" class="sidebar_widget__post__content__title">{{blog.title}}</n-link>
                    </div>
                </div>
            </div>
        </div>
        <!-- Sidebar Widget End -->

        <!-- Sidebar Widget Start -->
        <div class="sidebar_widget">
            <h3 class="sidebar_widget__title">Category</h3>
            <ul class="sidebar_widget__link">
                <li class="pb-3 last:pb-0" v-for="(blog, imageIndex) in blogData" :key="imageIndex">
                    <n-link class="sidebar_widget__linkcat" :to="`/blog/${slugify(blog.title)}`">{{blog.category}}</n-link>
                </li>
            </ul>
        </div>
        <!-- Sidebar Widget End -->

        <!-- Sidebar Widget Start -->
        <div class="sidebar_widget">
            <h3 class="sidebar_widget__title">tags</h3>
            <span class="sidebar_widget_titleborder"></span>
            <div class="sidebar_widget__link flex gap-2 flex-wrap">
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Appartment</n-link>
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Building</n-link>
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Luxuary</n-link>
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Property</n-link>
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Theme</n-link>
                <n-link class="text-black bg-light text-[13px] leading-[1.2] flex py-[10px] px-[20px] tracking-[0.4px] capitalize hover:text-white hover:bg-primary transition-all duration-500" to="/">Wordpress</n-link>
            </div>
        </div>
        <!-- Sidebar Widget End -->
    </div>
</template>
<script>
import blogData from '@/data/blogdata.json'
export default {
    data() {
        return {
            blogData
        }
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
    .sidebar {
        &_widget {
            @apply mb-[30px] last:mb-[0px] relative p-5 md:p-7 xl:p-9 border-2 border-[#F7F5F1];
            &__title {
                @apply mb-6 text-lg font-bold text-black relative uppercase;
            }
            &__search{
                @apply relative;
                &__input {
                    @apply border-b-1 border-[#000000] h-[50px] w-full py-[10px] pr-[40px] transition-all focus:outline-0 text-[#999] text-sm;
                }
                &__btn{
                    @apply absolute right-[2px] top-3 text-center transition-all hover:text-primary hover:transition-all text-[20px];
                }
            }
            &__link{
                & li {
                    @apply relative mb-2;
                }
                &__list{
                    @apply flex justify-between;
                }
            }
            &__post{
                @apply flex flex-wrap gap-[20px] mb-6 last:mb-0;
                &__thumb {
                    @apply w-[80px] block overflow-hidden bg-primary h-full;
                    & img {
                        @apply w-full object-cover object-center;
                    }
                }
                &__content {
                    @apply flex-1;
                    &__title {
                        @apply text-base font-medium tracking-[0.4px] text-black leading-[1.2] block transition-all hover:text-primary;
                    }
                }
            }
            &__linkcat{
                @apply relative pl-5 before:absolute before:content-[''] before:w-2 before:h-2 before:border-2 before:border-primary before:rounded-full before:left-0 before:top-1/2 before:-translate-y-1/2 hover:before:bg-primary hover:before:transition-all hover:before:duration-500;
            }
        }
    }
</style>