<template>

    <div class="my_buttons">
        <div class='consumetime'>{{detail.other}}</div>
    </div>
</template>
<script>
    export default {
        // data() {
        //     return {
        //         detial: {}
        //     }
        // },
        props: {
            detail: {
                type: Object,
                required: true
            }
        }
    }
</script>
<style scoped>
    .my_buttons{
        position: absolute;
        top:-10px;
        height: 40px;
        /* left: 0px; */
        width: 100%;
        display: flex;
        margin-right: -15px;
    }
    .my_buttons>.organization {
        /* float: left;
        display: inline; */
        flex:none;
        width: 80px;
        background: #e74c3c;
        font-size: 14px;
        font-weight: 600;
        padding: 10px 15px;
        color: #ffffff;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
    }

    .my_buttons>.consumetime {
        /* float: left;
        display: inline; */
        flex:1;
        background: #d16f1f;
        font-size: 14px;
        font-weight: 600;
        padding: 10px 15px;
        color: #ffffff;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        text-align: center;
        position: absolute;
        width: 100%;
        height: 35px;
        top: -20px;
    }
</style>
