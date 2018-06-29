<template>
    <div id="content">
        <centernavbar></centernavbar>
        <div class="container">            
            <div class="col-md-3" v-for="user in users">
                <photoframe v-bind:person=user></photoframe>
            </div>

        </div>
    </div>
</template>
<script>
    import photoframe from "./photoframe.vue";
    import centernavbar from "./center-navbar.vue";
    export default {
        components: {
            photoframe,
            centernavbar
        },
        data() {
            return {
                users: []
            };

        },
        mounted: function () {
            this.users.push({
                level: "import",
                img_rul: '',
                name: '主任A',
                desc: '带班主任',
                group:'室主任',
                duty:'带班主任'
            });
            this.users.push({
                level: "norm",
                img_rul: '',
                name: '值班员A',
                desc: '风暴潮 主班',
                group:'风暴潮',
                duty:'主班'
            });
            this.users.push({
                level:"norm",
                img_rul: '',
                name: '值班员B',
                desc: '风暴潮 副班',
                group:'风暴潮',
                duty:'副班'
            });
            this.users.push({
                level:"norm",
                img_rul: '',
                name: '值班员C',
                desc: '风暴潮 24小时岗',
                group:'风暴潮',
                duty:'24小时岗'
            });
            this.users.push({
                level:"norm",
                img_rul: '',
                name: '值班员D',
                desc: '风暴潮 警报班',
                group:'风暴潮',
                duty:'警报班'
            });
        }
    }
</script>
<style scoped>
    #content {
        background-color: rgba(0, 68, 255, 0.109);
        /* margin-left: 350px;
        margin-top:100px;
        margin-right: 0px; */
        bottom: 0px;
        top: 200px;
        right: 0px;
        left: 350px;
        /* margin-right: 0px; */
        /* width: 100%; */
        /* height: 100%; */
        position: fixed;
        z-index: 2;
        /* background: url(../img/content-background.jpg);
        background-size: 100% 100%;
        background-repeat: no-repeat; */
    }
    .container{
        margin-top: 0px;
    }
</style>
