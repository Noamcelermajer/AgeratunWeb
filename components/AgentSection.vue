<template>
    <div class="flex flex-col lg:flex-row lg:gap-y-0 gap-y-10">
        <div class="column-left">
            <div class="sidebar-text flex flex-col">
                <SectionTitle
                    secTionMargin="mb-10"
                    subTitle="Contact Agent"
                    titleClass="hidden"
                />
                <div class="agent" v-for="(member, index) in teamData.slice(0, 1)" :key="index">
                    <div class="agent-thumb mb-6 h-[120px] w-[120px] rounded-full overflow-hidden"><img :src="member.image" alt="A. Robertson"></div>
                    <div class="agent-content">
                        <h3 class="agent-name text-2xl leading-[1] mb-0">{{member.membername}}</h3>
                        <span class="agent-designation text-[13px]">{{member.membersubtitle}}</span>
                        <ul class="agent-info mt-7">
                            <li v-for="(info, index) in member.infoData.slice(0, 2)" :key="index">{{info.infotext}} <a :href="info.infolink">{{info.infonumber}}</a></li>
                        </ul>
                        <n-link :to="`/team/${slugify(member.membername)}`" class="mt-7 text-sm leading-[1] realtive inline-block uppercase text-black border-b-1 border-[#8D8D91] transition-all hover:text-primary hover:border-primary">See Profile</n-link>
                    </div>
                </div>
            </div>
        </div>

        <div class="column-right">
            <div class="">
                <h2 class="content-block-title">Subscribe for Project Information</h2>
                <ul class="feature-list flex flex-wrap flex-col md:flex-row mb-10 md:mb-16">
                    <li v-for="(item, imageIndex) in items" :key="imageIndex" class="text-lg pb-6 last:pb-0 relative table md:w-1/2 pl-10 text-black last:mb-0 before:content-['\f12d'] before:font-[flaticon] before:text-xs before:absolute before:top-0 md:before:top-1 before:left-0 before:w-6 h-6 before:text-center before:text-white before:rounded-full before:bg-primary before:leading-[24px]">{{item.title}}</li>
                </ul>
                <form id="contact-form" 
                    class="grid gap-x-10 grid-cols-2" 
                    action="https://getform.io/f/6af30b8c-e767-4d30-b964-d7e38d35078b" 
                    method="POST">
                    <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                        <input type="text" class="text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Name">
                    </div>
                    <div class="single-fild col-span-2 sm:col-span-1 mb-5">
                        <input type="text" class=" text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Phone">
                    </div>
                    <div class="single-fild col-span-2 mb-5">
                        <input type="email" class=" text-[15px] relative block w-full h-[50px] py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="E-mail">
                    </div>
                    <div class="single-fild col-span-2">
                        <textarea class="h-32 mb-6 text-[15px] relative block w-full py-4 transition-all duration-500 text-[#515151] border-t-0 border-x-0 border-b-1 border-[#cfcfd4] rounded-[4px] bg-transparent focus:border-t-0 focus:border-x-0 focus:border-black focus:shadow-none focus-visible:outline-0" placeholder="Write from here" spellcheck="false" data-gramm="false"></textarea>
                        <div class="flex justify-start w-full md:mt-10">
                            <button type="submit" value="submit" name="submit" class="btn btn-md btn-light btn-hover-primary max-w-[150px] md:max-w-[200px] w-full">Submit</button>
                            <p class="form-messege"></p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import teamData from '@/data/teamdata.json'
export default {
    components: {
        SectionTitle: () => import('@/components/title/SectionTitle')
    },
    data () {
        return {
            teamData,
            items: [
                {
                    title: "High quality file of apartment plan"
                },
                {
                    title: "Incentive policy directly from the investor"
                },
                {
                    title: "Latest updated price list"
                },
                {
                    title: "Schedule to visit the model apartment"
                },
                {
                    title: "Get notified about the opening sale date"
                }
            ]
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
.btn {
    @apply z-20 before:content-[""] before:absolute before:right-0 before:top-0 before:w-[200%] before:h-[200%] before:transition-all before:duration-700 before:-z-10 before:rounded-[0%] uppercase before:opacity-0 hover:before:opacity-100;
}
.btn-md {
    @apply text-dark h-[60px] px-[30px] py-[15px] text-[14px] leading-[1] relative inline-block overflow-hidden items-center transition-all duration-700;
}
.btn-hover-primary {
    @apply hover:border-[#0EA478] hover:text-white before:bg-[#0EA478] hover:transition-all hover:duration-700;
}
.btn-light {
    @apply bg-white;
}
</style>