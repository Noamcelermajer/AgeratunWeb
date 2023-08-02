<template>
    <div>
        <ul class='mobilemenu'>
            <li v-for='(link, i) in menuData' :key='i'>
                <n-link class="mobilemenu_link text-white py-3 block pl-5" :to="link.url">
                    {{ link.name }}
                </n-link>
                <span class='submenu-toggle' v-if="link.submenu">
                    <i class="fi fi-down-arrow"></i>
                </span>
                <ul class="submenu" v-if="link.submenu">
                    <li v-for='(link, i) in link.submenu' :key='i' class="titlelink">
                        <n-link class="text-white font-normal pl-10 py-3 block" :to="link.url"> {{ link.name }} </n-link>
                        <span class='submenu-toggle' v-if="link.submenu">
                            <i class="fi fi-down-arrow"></i>
                        </span> 
                        <ul class="submenu" v-if="link.submenu">
                            <li v-for='(link, i) in link.submenu' :key='i'>
                                <n-link class="text-white font-normal pl-5 py-3 block" :to="link.url"> {{ link.name }} </n-link>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script>
import menuData from "@/data/menudata.json";
    export default {
        data() {
            return {
                menuData
            }
        },
        mounted() {
            let getSiblings = function (e) {
                let siblings = [];
                if(!e.parentNode) {
                    return siblings;
                }
                let sibling  = e.parentNode.firstChild;
                while (sibling) {
                    if (sibling.nodeType === 1 && sibling !== e) {
                        siblings.push(sibling);
                    }
                    sibling = sibling.nextSibling;
                }
                return siblings;
            };

            const subMenuToggle = document.querySelectorAll('.submenu-toggle');
            subMenuToggle.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    if(!this.classList.contains('active')) {
                        this.classList.add('active')
                        this.nextElementSibling.classList.add('active')
                        this.closest('li').classList.add('active')
                        getSiblings(this.closest('li')).forEach(function(item) {
                            item.classList.remove('active')
                            item.querySelectorAll('li, .submenu-toggle, .submenu').forEach(function(child) {
                                child.classList.remove('active')
                            })
                        })
                    } else {
                        this.closest('li').classList.remove('active')
                        this.closest('li').querySelectorAll('li, .submenu-toggle, .submenu').forEach(function(child) {
                            child.classList.remove('active')
                        })
                    }
                })
            })
        }
    }
</script>

<style lang='scss' scoped>
    .mobilemenu {
        @apply py-10;
        li {
            @apply relative last:mb-0 border-t-1 border-white border-opacity-[0.15];
        }
        .submenu {
            @apply opacity-0 invisible hidden h-0 transition duration-300;
            &.active {
                @apply opacity-100 visible block h-full transition duration-300;
            }
            li {
                &.title {
                    @apply text-sm;
                    a {
                        @apply font-medium;
                    }
                }
                .submenu {
                    li {
                        a {
                            @apply leading-[25px] font-normal text-sm;
                        }
                    }
                }
            }
        }
        .submenu-toggle {
            @apply w-[50px] h-[50px] bg-[#f3f3f3] bg-opacity-10 text-center text-base absolute right-0 top-0 cursor-pointer flex justify-center items-center transition-all;
            i {
                @apply transition-all duration-500 leading-[1] text-xs text-white;
            }
            &.active {
                i {
                    @apply transform -rotate-180 transition-all duration-500;
                }
            }
        }
    }
</style>