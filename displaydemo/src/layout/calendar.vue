<template>
    <div class="topcalendar">
        {{dateStr}}
        <!-- <div class="year">2018年</div>
        <div class="month">7月</div>
        <div class="day">2日</div> -->
    </div>
</template>
<script>
    export default {
        props:{
            dateStr:String
        }
    }
</script>
<style>
    * {
        margin: 0px;
        padding: 0px
    }

    .topcalendar {
        position: absolute;
        bottom: 10px;
        right: 150px;

        color: whitesmoke;
        /* color: rgb(229, 233, 25); */
        font-weight: 500;
        font-size: 40px;
        /* margin: 0;
        padding: 0; */
    }

    .topcalendar div {
        display: inline;
        color: whitesmoke;
        font-weight: 500;
        font-size: 40px;
        margin-left: -10px;
        width: 50px;
        height: 40px;
        /* margin: 0;
        padding: 0; */
    }

    .topcalendar div.year {
        background-color: #13cf91;

    }

    .topcalendar div.month {
        background-color: #14cfc0;

    }

    .topcalendar div.day {
        background-color: #14aacf;

    }
</style>