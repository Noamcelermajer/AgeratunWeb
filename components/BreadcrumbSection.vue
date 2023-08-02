<template>
    <div class="container-fluid">
        <div class="breadcrumb" :class="borderClass">
            <!-- Page Banner Start -->
            <div class="breadcrumb_banner">
                <ul class="breadcrumb_meta" :class="centerClass">
                    <li> <n-link class="relative before:absolute before:content-['/'] before:-top-[3px] before:-right-3" to="/">Home</n-link> </li>
                    <li><span class="text-black">{{BreadcrumbSubTitle}}</span></li>
                </ul>
                <h2 class="breadcrumb_banner__title">{{BreadcrumbTitle}}</h2>
            </div>
            <!-- Page Banner End -->
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            BreadcrumbSubTitle: {
                type: String,
                required: false
            },
            BreadcrumbTitle: {
                type: String,
                required: false
            },
            borderClass: {
                type: String,
                required: false
            },
            centerClass: {
                type: String,
                required: false
            }
        },
        components: {
        }
    }
</script>

<style lang="scss" scoped>
    .breadcrumb {
        @apply lg:py-[100px] md:py-[80px] py-[60px];
        &_meta{
            @apply flex items-center gap-5 mb-3 md:mb-5 lg:mb-8;
            & li {
                @apply relative;
            }
        }
        &_banner {
            @apply text-left;
            &__title {
                @apply md:text-6xl sm:text-[40px] text-[30px] font-bold text-black mb-0 relative;
            }
        }
    }
</style>