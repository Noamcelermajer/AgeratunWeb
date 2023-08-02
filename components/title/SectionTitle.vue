<template>
    <div class="" :class="secTionMargin">
        <span class="text-sm leading-[1.714] block uppercase text-primary" :class="subtitleClass"> {{subTitle}} </span>
        <h2 :class="titleClass"> {{title}} </h2>
    </div>
</template>

<script>
    export default {
        props: {
            title: String,
            titleClass: String,
            subTitle: String,
            subtitleClass: String,
            secTionMargin: String
        }
    }
</script>

<style lang='scss'>
    
</style>