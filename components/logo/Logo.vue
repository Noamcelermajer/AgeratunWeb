<template>
    <div>
        <n-link :to="logLink">
            <img src="/images/logo/logo-light.svg" alt="Logo" width="180" height="45">
        </n-link>
    </div>
</template>
<script>
    export default {
        props: {
            logLink: String,
        }
    }
</script>