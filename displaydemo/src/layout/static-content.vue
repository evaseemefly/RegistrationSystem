<template>
    <div id="left-content" class="col-md-2">
        <div class="container">
            <div v-for="vip in vips">
                <photoframe v-bind:person=vip></photoframe>
            </div>

        </div>
    </div>
</template>
<script>
    import photoframe from "./photoframe.vue";
    export default {
        components: {
            photoframe,
        },
        data() {
            return {
                vips: []
            };
        },
        compiled: () => {

        },
        mounted: () => {

        },
        mounted: function () {
            var myself = this;
            this.vips.push({
                level:"urgency",
                img_rul: '',
                name: '易小雷',
                desc:'带班领导',

            });
            this.vips.push({
                level:"minor",
                img_rul: '',
                name: '领导B',
                desc:'应急管理值班岗',
            });
        }
    }
</script>
<style scoped>
.container{
    margin-top:15px;
}
    #left-content {
        left: 0px;
        top:200px;
        /* margin-left: 0px;
        margin-top: 130px; */
        /* margin-bottom:0px; */
        width:350px;
        height: 100%;
        position: fixed;
        z-index: 2;
        background-color: rgba(3, 45, 184, 0.493);
    }
</style>
