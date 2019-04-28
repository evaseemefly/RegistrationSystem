<template>
  <div id="mycontent">
    <staticcontent :nowDate="nowDate"></staticcontent>
    <maincontent :nowDate="nowDate"></maincontent>
  </div>
</template>
<script>
// import maincontent from "./layout/main-content.vue";
// import staticcontent from "./layout/static-content.vue";
import maincontent from "./main-content.vue";
import staticcontent from "./static-content.vue";
import getPersonList from "../api/api.js";
import bus from "../assets/eventBus.js";
// import x from "../api/api.js"
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
      finial_objs: [],
      nowDate: null,
      interval: 1000 * 30
    };
  },
  methods: {
    //读取人员信息列表
    loadPersonList: function() {
      var myself = this;

      function page(index, count) {
        this.pageIndex = index;
        this.pageCount = count;
      }

      function Detail(color, img_url) {
        //显示中的详细信息
        this.color = color;
        this.img_url = img_url;
      }
      //此方法不再使用了
      getPersonList().then(res => {
        //注意此时返回的data中包含now_date与persons
        // finial_objs = [];
        //分别取出时间与persons
        var nowDate = myself.nowDate;
        var persons = myself.persons;
        //获取person list长度
        var pagelist_count = myself.listcount;
        //当前页码
        var page_index = myself.pageindex;

        //总页数
        //丢弃小数部分,保留整数部分
        //count=parseInt(data.listcount/page_count)
        //向上取整,有小数就整数部分加1
        var footer_count = Math.ceil(myself.listcount / page_count);
        $(persons).each(function(index, element) {
          var url_img = `/static/img/${element.department}/${element.name}.jpg`;
          // "/static/img/" + element.department + "/" + element.name +".jpg"
          var element = new Detail(dic[element.job], url_img);
          // element.color = dic[element.job];
          // element.img_url = "/static/img/" + element.department + "/" + element.name +
          //     ".jpg"
          myself.finial_objs.push(element);
        });
      });
    },
    //为时间赋值
    initNowDate: function() {
      // this.nowDate = new Date();
      // this.nowDate=moment();
      var myself = this;
      this.nowDate = this.moment();

      bus.$emit("on-reloadDate", myself.nowDate);
    },
    //重新加载页面
    reaload: function() {
      window.location.reload();
    }
  },
  // mounted: function() {
  // 	// this.initNowDate();
  // },
  created: function() {
    var myself = this;
    this.initNowDate();
    setInterval(myself.initNowDate, myself.interval);

    //定期刷新页面
    // var timer = window.setInterval(myself.reaload, myself.interval);
  }
};
</script>
<style>
#mycontent {
  bottom: 0px;
  /* 最终实现版v1 */
  top: 100px;
  /* 最终实现版v2 */
  /* top: 150px; */
  right: 0px;
  left: 0px;
  position: fixed;
  z-index: -10;
  /* 实现样式1 */
  background: url("../img/other/background_1.jpg");
  /* 实现样式2：比较丑的图片 */
  /* background: url('../img/content-background.jpg'); */
  background-size: cover;
  /* 加入透明滤镜 */
  /* filter: opacity(60%); */
  /* background: url(../img/content-background.jpg); */
  /* background-size: 100% 100%;
    background-repeat: no-repeat; */
}
</style>