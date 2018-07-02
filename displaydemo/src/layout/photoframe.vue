<template>
    <div>
        <div class="post-container">
            <div class="post-title">{{person.desc}}</div>
            <div class="post-module">
                <div class="my_frame">
                    <img v-bind:src="person.img_url">
                </div>
                <div class="post-content" :class=person.level>
                    <photobutton v-show="isShowButton(person)" :detail=person></photobutton>
                    <h1 class="title">{{person.name}}</h1>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import photobutton from "./photo-button.vue";
    export default {
        data() {
            return {
                level_dict: [
                    "urgency", "minor"
                ]
            }
        },
        components: {
            photobutton
        },
        methods:{
            isShowButton(item){
                var isShow=true;
                if(this.level_dict.indexOf(item.level)>=0)
                {
                    isShow=false;
                }
                // if(item.level in this.level_dict){
                //     isShow=true;
                // }
                return isShow;
            }
        },
        props: {
            person: {
                type: Object,
                required: true
            }
        },
        // props:['person'],
    }
</script>
<style>
    @import "../assets/styles/post-module.css";

    .post-module {
        margin-bottom: 20px;
    }

    .norm {
        background-color: #ffffff;
    }

    .import {
        background-color: #ffffff;
        /* background: linear-gradient(left bottom,red,white); */
        /* background-color:linear-gradient(right,red,white); */
        /* background-color: rgba(3, 87, 182, 0.575)  */
    }

    .urgency {
        background-color: #ffffff;
        /* background-color: rgba(182, 3, 182, 0.575)  */
        /* background: linear-gradient(left bottom,blue,white); */
        /* background-color:linear-gradient(right,blue,white); */
    }

    .minor {
        background-color: #ffffff;
        /* background-color: rgba(3, 146, 182, 0.575)  */
        /* background: linear-gradient(left bottom,yellowgreen,white); */
        /* background-color:linear-gradient(right,yellowgreen,white); */
    }
</style>
