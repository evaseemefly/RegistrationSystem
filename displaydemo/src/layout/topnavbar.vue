<template>
    <nav id="my-top-navbar" class="navbar navbar_myself navbar-default navbar-fixed-top">
        <calendar :dateStr=nowDateStr></calendar>
        <img src='../img/logo.png' class="logo">
        <!-- <div class='logo'></div> -->
        <!-- <div class="navbar-header" id="my_navbar">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse">
                <span class="sr-only">Toggle navigation</span>
            </button>
            <a class="navbar-brand" href="#">预报中心九楼值班系统</a>
            <a class="navbar-brand" href="#">值班信息</a>
        </div> -->
        <!-- <div class="FlexInner">国家海洋环境预报中心</div>
        <div class="FlexInner">值班信息</div> -->
    </nav>
</template>
<script>
import calendar from "./calendar.vue";
import bus from "../assets/eventBus.js";
export default {
  components: {
    calendar
  },
  data() {
    return {
      nowDate: null
    };
  },
  computed: {
    nowDateStr: function() {
      if (this.nowDate == null) {
        return "";
      } else {
        // var dateStr =
        //   this.nowDate.getFullYear() +
        //   this.nowDate.getMonth() +
        //   this.nowDate.getDate();
        var dateStr= this.nowDate.format('YYYY-MM-DD')
        return dateStr;
      }
    }
  },
  created: function() {
    var myself = this;
    // 注意此处的事件总成，若写在computed事件中，则不会执行后面的钩子函数
    bus.$on("on-reloadDate", (msg) => {
        console.log(msg);
      myself.nowDate = msg;
    });
    // bus.$on("on-reloadDate", function(msg) {
    //   myself.nowDate = msg;
    // });
    //   myself.timer=setInterval(function(){
    //       myself.date=new Date();
    //   },)
  },
  beforeDestroy() {
    bus.$off("on-reloadDate");
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

  /* background: linear-gradient(left top,rgba(13, 71, 231, 0.856),rgba(11, 105, 160, 0.746)); */
  /* 最终实现版v1 */
  /* background: linear-gradient(30deg,#34495e, #1abc9c ); */
  /* 最终实现版v2 */
  /* background:linear-gradient(135deg,#32607ed3 25%,#4f9accd8 75%);  */
  /* 最终实现版v3 */
  background: url(../img/topbar-background.jpg);
  background-size: 100% 100%;
  background-repeat: no-repeat;
  /* 最终实现版v1 */
  /* height: 100px; */

  /* 最终实现版v2 */
  height: 150px;
  display: flex;
  justify-content: center;
  /* 设置交叉轴上如何对其 */
  align-items: flex-end;
}
.navbar_myself > .logo {
  float: left;
  height: 90px;
  position: absolute;
  right: 30px;
  bottom: 30px;

  /* src:url(../img/logo.png); */
  /* src:"../img/logo.png"; */
  /* background: url(../img/logo.png); */
}
.navbar_myself > .FlexInner {
  /* background-color: rgb(152, 199, 22); */
  display: flex;
  color: rgb(229, 233, 25);
  height: 80px;
  font-family: "Oswald", sans-serif;
  /* 加入文字阴影 */
  /* text-shadow: 2px 2px 10px grey; */
  text-shadow: 2px 2px 10px #000;
  /* text-shadow: 2px 2px white,
                     6px 6px rgba(50,50,50,.25); */
  font-weight: 700;
  font-size: 2.5em;
  width: 40%;
}
</style>