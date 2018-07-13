<template>
    <div>
        <div class="topcenterbar">
            <a href="#" class="current">预警室</a>
            <a href="#">海啸室</a>
            <a href="#">环境室</a>
            <a href="#">气象室</a>
            <a href="#">极地室</a>
            <a href="#">气候室</a>
            <a href="#">数值室</a>
            <a href="#">网络部</a>
            <a href="#">产品部</a>
            <a href="#">信息室</a>
            
        </div>
        <!-- <nav class="navbar navbar-center">
            <div class="container-fluid">
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li class="active">
                            <a href="#">预警室
                                <span class="sr-only">(current)</span>
                            </a>
                        </li>
                        <li>
                            <a href="#">气象室</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav> -->
    </div>
</template>
<script>
    export default {

    }
</script>
<style scoped>
    .navbar-center {
        background-color: rgba(0, 57, 245, 0.089);
        margin-bottom: 2px;
    }

    .topcenterbar {
        text-align: center;
        height: 65px;
        color: rgb(213, 214, 226);
        font-weight: 500;
        font-family: "Microsoft YaHei", 宋体, "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
        background: rgba(73, 74, 95, 0.438);
    }

    .topcenterbar a {
        display: inline-block;
        margin: 0.5em;
        padding: 0.6em 1em;
        border: 3px solid #fff;
        font-weight: 700;
        color: #fff;
    }

    .topcenterbar a.current {
        background: #1d7db1;
        color: #fff;
    }

    /* a {
        color: aliceblue;
        font-size: large;
        font-weight: 300;
    } */
</style>
