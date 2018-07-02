<template>
    <nav class="navbar navbar_myself navbar-default navbar-fixed-top">
        <div class="navbar-header" id="my_navbar">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse">
                <span class="sr-only">Toggle navigation</span>
            </button>
            <calendar></calendar>
            <!-- <a class="navbar-brand" href="#">预报中心九楼值班系统</a>
            <a class="navbar-brand" href="#">值班信息</a> -->
        </div>
    </nav>
</template>
<script>
    import calendar from "./calendar.vue";
    export default {
        components: {
            calendar
        }
    }
</script>

<style scoped>
    .navbar_myself div a {
        font-family: "Microsoft YaHei";
        color: #f7fcfb;
    }

    .navbar_myself {
        background-color: rgba(1, 32, 100, 0.746);
        /* height: 100px; */
        background: url(../img/topbar-background.jpg);
        background-size: 100% 100%;
        background-repeat: no-repeat;
        height: 200px;
    }
</style>
