<template>
    <!-- Menu Start -->
    <div class="hidden lg:block">
        <ul class="mainmenu">
            <li class="mainmenu_list group" v-for='(link, i) in menuData' :key='i'>
                <NuxtLink :to="link.url" class="mainmenu_link" :class="textClass">{{ link.name }}</NuxtLink>
                <ul class="submenu" v-if="link.submenu">
                    <li class="submenu_list" v-for='(link, i) in link.submenu' :key='i'>
                        <NuxtLink :to="link.url" class="submenu_link"> {{ link.name }} </NuxtLink>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    <!-- Menu End -->
</template>

<script>
    import menuData from '@/data/menudata.json'
    export default {
        props: {
            textClass: {
                type: String,
                required: false,
            }
        },
        data () {
            return {
                menuData
            }
        }
    }
</script>

<style lang="scss" scoped>
    .is-sticky{
        .mainmenu {
            &_link {
                &.sticky-height{
                    @apply py-8;
                }
            }
        }
    }
    .mainmenu {
        &_list {
            @apply inline-block relative mr-6 xl:mr-12 text-[14px];
        }
        &_link {
            @apply block py-[45px] text-[14px] font-bold uppercase leading-[2.14] font-body;
        }
    }
    .submenu {
        @apply w-[180px] shadow-[0_0px_3px_rgba(0,0,0,0.3)] absolute opacity-0 invisible group-hover:opacity-100 group-hover:visible top-[100%] bg-white py-4 z-30 transition-all duration-300 group-hover:transition-all group-hover:duration-500;
        &_list {
            @apply block mb-[10px] pb-[10px] last:mb-0 border-b-1 border-bordercolor border-opacity-30 last:pb-0 last:border-0 px-4;
        }
        &_link {
            @apply font-medium text-left capitalize text-sm text-black hover:text-primary;
        }
    }
</style>