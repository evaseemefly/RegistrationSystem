<template>
    <div id="mycontent">
        <staticcontent></staticcontent>
        <maincontent></maincontent>
    </div>
</template>
<script>
    // import maincontent from "./layout/main-content.vue";
    // import staticcontent from "./layout/static-content.vue";
    import maincontent from "./main-content.vue";
    import staticcontent from "./static-content.vue";
    import getPersonList from "../api/api.js";
    export default {

        components: {
            maincontent,
            staticcontent
        },
        data() {
            return {
                items: [],
                page_index: 0,
                pagelist_count: 12,
                footer_count: 2,
                //显示要素集合
                finial_objs:[]
            }
        },
        methods: {
            loadPersonList: function () {
                var myself=this;
                function page(index, count) {
                    this.pageIndex = index;
                    this.pageCount = count;
                }
                function Detail(color,img_url){
                    //显示中的详细信息
                    this.color=color;
                    this.img_url=img_url;
                }
                getPersonList().then(res => {
                    //注意此时返回的data中包含now_date与persons
                    // finial_objs = [];
                    //分别取出时间与persons
                    now_date = myself.now_date
                    persons = myself.persons
                    //获取person list长度
                    pagelist_count = myself.listcount
                    //当前页码
                    page_index = myself.pageindex

                    //总页数
                    //丢弃小数部分,保留整数部分
                    //count=parseInt(data.listcount/page_count)
                    //向上取整,有小数就整数部分加1
                    footer_count = Math.ceil(myself.listcount / page_count)
                    $(persons).each(function (index, element) {
                        var url_img=`/static/img/${element.department}/${element.name}.jpg`
                        // "/static/img/" + element.department + "/" + element.name +".jpg"
                        var element=new Detail(dic[element.job],url_img)
                        // element.color = dic[element.job];
                        // element.img_url = "/static/img/" + element.department + "/" + element.name +
                        //     ".jpg"
                        myself.finial_objs.push(element)
                    })
                })
            }

        }
    }
</script>
<style>
    #mycontent {
        bottom: 0px;
        top: 200px;
        right: 0px;
        left: 0px;
        position: fixed;
        background: url(../img/content-background.jpg);
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }
</style>