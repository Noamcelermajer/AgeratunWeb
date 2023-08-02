<template>
    <div>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-7">
            <div class="" v-for="(member, index) in teamData" :key="index">
                <n-link class="block overflow-hidden bg-primary group" :to="`/team/${slugify(member.membername)}`">
                    <img class="group-hover:opacity-40 transition duration-500 group-hover:transform w-full" :src="member.image" alt="Team-image">
                </n-link>
                <div class="py-[25px] px-[30px] lg:px-[20px] xl:px-[30px] bg-white">
                    <n-link :to="`/team/${slugify(member.membername)}`" class="xl:text-[24px] text-[20px] leading-[1.25] mb-1 font-bold text-black">{{member.membername}}</n-link>
                        <span class="text-[13px] leading-[20px] block mb-5">{{member.membersubtitle}}</span>
                    <ul>
                        <li v-for="(info, index) in member.infoData.slice(0, 2)" :key="index" class="text-[#999999] text-[13px] xl:text-[15px]">
                            {{info.infotext}} <a class="text-black hover:text-primary" :href="info.infolink">{{info.infonumber}}</a>
                        </li>
                    </ul>
                    <ul class="team-social flex gap-[18px] mt-4">
                        <li v-for="(social, index) in member.socialData" :key="index">
                            <a class="text-[16px] text-[#999999]" :href="social.link" target="_blank"><i :class="social.icon"></i></a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import teamData from '@/data/teamdata.json'
    export default {
        data () {
            return {
                teamData,
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

</style>