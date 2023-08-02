<template>

    <!-- Advantages Section Start -->
    <div class="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-9">
        <div v-for="(item, imageIndex) in items" :key="imageIndex" class="group">
            <div class="relative overflow-hidden bg-primary">
                <img class="group-hover:opacity-40 group-hover:transform group-hover:transition-all group-hover:duration-500 transition-all duration-500" :src="item.imgCount" alt="Count">
            </div>
            <div class="lg:pt-9 pt-7">
                <h2 class="2xl:text-4xl xl:text-3xl text-2xl mb-3">{{item.title}}</h2>
                <p class=" text-[15px]">{{item.text}}</p>
            </div>
        </div>
    </div>
    <!-- Advantages Section End -->

</template>
<script>
    export default {
        data () {
            return {
                items: [
                    {
                        imgCount: "/images/advantages/advantage-1.jpg",
                        title: "World-Class Architecture",
                        text: "Designed by Baroque Arch Studio in Poland, is an internationally acclaimed architects office."
                    },
                    {
                        imgCount: "/images/advantages/advantage-2.jpg",
                        title: "Location in Manhattan",
                        text: "Located in a prime location of Manhattan district, connected to many works and convenient transportation"
                    },
                    {
                        imgCount: "/images/advantages/advantage-3.jpg",
                        title: "Over 20 Amenities",
                        text: "Over 20 amenities to help enhance the quality of life to residencer as pools, schools, market, park, playground, etc"
                    }
                ]
            }
        }
    }
</script>