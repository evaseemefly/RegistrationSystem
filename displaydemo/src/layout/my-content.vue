<template>
    <div id="mycontent">
        <staticcontent></staticcontent>
        <maincontent></maincontent>
    </div>
</template>
<script>
    // import maincontent from "./layout/main-content.vue";
    // import staticcontent from "./layout/static-content.vue";
    import maincontent from "./main-content.vue";
    import staticcontent from "./static-content.vue";
    export default {

        components: {
            maincontent,
            staticcontent
        }
    }
</script>
<style>
    #mycontent {
        bottom: 0px;
        top: 200px;
        right: 0px;
        left: 0px;
        position: fixed;
        background: url(../img/content-background.jpg);
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }
</style>
