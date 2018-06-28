<template>
    <div>
        <div class="post-container">
            <div class="post-title">{{person.desc}}</div>
            <div class="post-module">
                <div class="my_frame">
                    <img v-bind:src="person.img_url">
                </div>
                <div class="post-content" :class=person.level>
                    <h1 class="title">{{person.name}}</h1>
                    <div class="my-bottons">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        // data(){
        //     return{
        //         person:{}
        //     }
        // },
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
    .norm{
        background-color: #ffffff;
    }
    .import{
        background-color: #ffffff;
        /* background: linear-gradient(left bottom,red,white); */
        /* background-color:linear-gradient(right,red,white); */
        /* background-color: rgba(3, 87, 182, 0.575)  */
    }
    .urgency{
        background-color: #ffffff;
        /* background-color: rgba(182, 3, 182, 0.575)  */
        /* background: linear-gradient(left bottom,blue,white); */
        /* background-color:linear-gradient(right,blue,white); */
    }
    .minor{
        background-color: #ffffff;
        /* background-color: rgba(3, 146, 182, 0.575)  */
        /* background: linear-gradient(left bottom,yellowgreen,white); */
        /* background-color:linear-gradient(right,yellowgreen,white); */
    }
</style>
