<template>
    <nav id="my-top-navbar" class="navbar navbar_myself navbar-default navbar-fixed-top">
        <!-- <div class="navbar-header" id="my_navbar">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse">
                <span class="sr-only">Toggle navigation</span>
            </button>
            <a class="navbar-brand" href="#">预报中心九楼值班系统</a>
            <a class="navbar-brand" href="#">值班信息</a>
        </div> -->
        <div class="FlexInner">国家海洋环境预报中心</div>
        <div class="FlexInner">值班信息</div>
    </nav>
</template>
<script>
    // import calendar from "./calendar.vue";
    export default {
        components: {
            // calendar
        }
    };
</script>

<style scoped>
    /* #my-top-navbar {
  position: absolute;
  top: 0px;
} */
    .navbar_myself div a {
        font-family: "Microsoft YaHei";
        color: #f7fcfb;
    }

    .navbar_myself {
        /* background-color: rgba(13, 71, 231, 0.856); */
        
        /* background: linear-gradient(30deg,rgba(11, 26, 160, 0.746), rgba(11, 105, 160, 0.746) ); */
        /* height: 100px; */
        /* background: url(../img/topbar-background.jpg); */
        /* background: linear-gradient(left top,rgba(13, 71, 231, 0.856),rgba(11, 105, 160, 0.746)); */
        background: linear-gradient(30deg,rgba(11, 26, 160, 0.746), rgba(11, 105, 160, 0.746) );
        background-size: 100% 100%;
        background-repeat: no-repeat;
        height: 100px;
        display: flex;
        justify-content: center;
        /* 设置交叉轴上如何对其 */
        align-items: flex-end;

    }

    .navbar_myself>.FlexInner {
        /* background-color: rgb(152, 199, 22); */
        display: flex;
        color: rgb(229, 233, 25);
        height: 80px;
        font-family: 'Oswald', sans-serif;

        font-weight: 700;
        font-size: 2.5em;
        width: 40%;
    }
</style>