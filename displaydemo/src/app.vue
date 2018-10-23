<template>
    <div id="app">
        <topnavbar></topnavbar>
        <mycontent></mycontent>
        <!-- <maincontent></maincontent> -->
        <!-- <tabbar></tabbar> -->
        <!-- <topnavbar></topnavbar> -->
    </div>
</template>

<script>
    import maincontent from "./layout/main-content.vue";
    import staticcontent from "./layout/static-content.vue";
    import mycontent from "./layout/my-content.vue";
    // import tabbar from "./layout/tabbar.vue";
    import topnavbar from "./layout/topnavbar.vue";
    import watch from "./layout/watch.vue";

    export default {
        data() {
            return {
                searchResult: null
            }
        },
        //注意：需要在componetns中声明子组件，才能在上面显示
        components: {
            maincontent,
            staticcontent,
            // tabbar,
            topnavbar,
            watch,
            mycontent
        }
    }
</script>

<style>
    #app {
        background-color: brown;
    }
</style>
