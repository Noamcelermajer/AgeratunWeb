<template>
    <div class="grid grid-cols-1 gap-8 md:gap-10 lg:gap-14">
        <div class="blog_wrapper relative group" v-for="(blog, index) in getItems" :key="index">
            <n-link :to="`/blog/${slugify(blog.title)}`" class="block relative overflow-hidden bg-primary">
                <img class="group-hover:opacity-40 group-hover:transform group-hover:transition-all group-hover:duration-500 transition-all duration-500 w-full" :src="blog.bigimage" alt="Blog">
            </n-link>
            <div class="flex flex-col mt-6">
                <ul class="meta-top flex items-center gap-3 mb-4">
                    <li class="flex gap-3 after:content-[''] after:bg-[#cccccc] after:h-4 after:w-[1px] after:right-0 after:top-0 after:self-center">
                        <n-link :to="`/blog/${slugify(blog.title)}`" class="text-black text-sm font-normal uppercase relative hover:text-primary transition-all">{{blog.category}}</n-link></li>
                    <li class="text-sm">{{blog.date}}</li>
                </ul>
                <h3 class="md:text-2xl text-xl mb-4 leading-[1.25]">
                    <n-link class="hover:text-primary transition-all" :to="`/blog/${slugify(blog.title)}`">{{blog.title}}</n-link>
                </h3>
                <p class="text-[15px]">{{blog.blogText}}</p>
                <ul class="blog-meta flex mt-5 md:mt-8 flex-wrap gap-7">
                    <li class="text-sm flex gap-1"><i class="text-[24px] leading-[1] flex self-center fi fi-user"></i>By <n-link class="text-black hover:text-primary transition-all" :to="`/blog/${slugify(blog.title)}`">Ecostateusar</n-link></li>
                    <li class="text-sm flex gap-1"><i class="text-[24px] leading-[1] flex self-center fi fi-pulse-rate"></i>{{blog.totalview}} Views</li>
                </ul>
            </div>
        </div>
        
        <paginate
            :page-count="getPaginateCount"
            :prev-text="'<'"
            :next-text="'>'"
            :click-handler="paginateClickCallback"
            class="pagination-list">
        </paginate>
    </div>
</template>

<script>
    import blogData from '@/data/blogdata.json'
    export default {
        data () {
            return {
                blogData,
                currentPage: 1,
                perPage: 4,
            }
        },
        computed: {
            getItems() {
                let start = (this.currentPage - 1) * this.perPage;
                let end = this.currentPage * this.perPage;
                return this.blogData.slice(start, end);
            },
            getPaginateCount() {
                return Math.ceil(this.blogData.length / this.perPage);
            }
        },
        methods: {
            paginateClickCallback(pageNum) {
                this.currentPage = Number(pageNum);
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

<style lang="scss">
.pagination-list{
    @apply flex justify-center items-center mt-1 md:mt-8;
    li {
        &.disabled {
            @apply hidden;
        }
        &.active{
            & a {
                @apply bg-primary text-white;
            }
        }
        a {
            @apply w-[35px] h-[35px] text-[16px] flex justify-center items-center rounded-none mx-1 text-black text-center bg-transparent border-1 border-bordercolor hover:bg-primary;
        }
    }
}
</style>