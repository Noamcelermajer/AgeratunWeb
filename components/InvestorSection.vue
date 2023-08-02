<template>

    <div class="custom-column">

        <div class="column-left">
            <div class="sidebar-text flex flex-col gap-8">
                <div class="sidebar-text-item">
                    <h6 class="text-primary text-[14px] font-normal leading-[1.7] block uppercase">Investor and Development</h6>
                </div>
            </div>
        </div>

        <div class="column-right">
            <div class="content-block">
                <h2 class="content-block-title">Ecostate Park Residence was invested and developed by EcoGroup corporate.</h2>
                <div class="content-block-text">
                    <p class="mb-5">Established in 1991, EcoGroup corporate has much successfully accomplished with over 10,000,000 m2 of residential, tourism and industrial estate projects on worldwide. Become the the leading of real estate corporate in California.</p>
                    <p>Some top projects from Ecogroup as: <n-link class="text-primary underline" to="/service">EcoHaus Riverside Residential</n-link>, Ecopi Garden Bungalow, Ohio Skylight Building, Sixsen Resort Miami, Fusion Ecologde Floria, etc</p>
                </div>
            </div>
            <div class="relative">
                <div class="grid md:grid-cols-2 grid-cols-1 gap-6 lg:gap-10">
                    <div v-for="(investor, imageIndex) in investorData" :key="imageIndex" class="group flex flex-col max-w-[450px] pt-14 border-t-1 border-bordercolor">
                        <div class=" mb-4">
                            <a :href="investor.investorlink" target="_blank"><img :src="investor.images" alt="Image"></a>
                        </div>
                        <div class="counterup-content">
                            <h3 class="text-lg uppercase font-bold relative block mb-1 text-black">{{investor.projectname}}</h3>
                            <a class="text-[#0099ff] text-sm hover:text-primary hover:transition-all transition-all" :href="investor.investorlink" target="_blank">{{investor.investorweb}}</a>
                            <p class="text-[15px] mt-3">{{investor.investortext}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

</template>

<script>
    import investorData from '@/data/investordata.json'
    export default {
        data () {
            return {
                investorData
            }
        }
    }
</script>

<style lang="scss">

</style>