<template>
  <div id="content">
    <div class="background-line">
      <centernavbar class="my-top-navbar" @loadUserList="loadUserList"></centernavbar>
      <div class="container my-box">
        <!-- <div class="col-md-4 my-row" v-for="user in users"> -->
        <div class="my-row" v-for="user in users">
          <photoframe v-bind:person=user></photoframe>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getUserListByDepartment, getLevel } from "../api/api.js";
import { DepartmentMid, User } from "../common/model.js";
import photoframe from "./photoframe.vue";
import centernavbar from "./center-navbar.vue";
export default {
  components: {
    photoframe,
    centernavbar
  },
  props: {
    nowDate: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      users: [],
      selected_date: "",
      nowDate: null
    };
  },
  methods: {
    //加载userlist
    loadUserList: function (params) {
      var myself = this;

      //为当前时间赋值
      myself.selected_date = myself.nowDate.format('YYYY-MM-DD');
      myself.users = [];
      var mid_model = new DepartmentMid(params.did, myself.selected_date);
      getUserListByDepartment(mid_model).then(res => {
        // console.log(res)
        $.each(res.data, function (index, val) {
          var user_temp = new User(
            val.user.username,
            getLevel(val.user.level),
            val.rDepartmentDuty.duid.desc,
            val.rDepartmentDuty.did.derpartmentname,
            val.rDepartmentDuty.duid.dutyname,
            val.user.imgUrl
          );
          myself.users.push(user_temp);
        });
      });
    }
  },
  mounted: function () {
  }
};
</script>
<style scoped>
/* html,
body {
  background: linear-gradient(45deg, #3498db 25%, #16a085 50%);
  height: 100%;
} */
.background-line {
  /* background: linear-gradient(45deg, #3498db 25%rgb(22, 160, 132)85 50%); */
  /* 实现版v1 */
  background:linear-gradient(135deg,#32607e8f 25%,#0ac29dbd 75%); 
  /* 实现版v2 */
  /* background:linear-gradient(135deg,#32607e8f 25%,#4f9acc8f 75%);  */
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
#content {
  /* background-color: rgba(0, 68, 255, 0.109); */
  /* margin-left: 350px;
        margin-top:100px;
        margin-right: 0px; */
  bottom: 0px;
  /* 最终实现v1 */
  top: 100px;
  /* 最终实现v2 */
  /* top: 150px; */
  right: 0px;
  left: 350px;
  /* margin-right: 0px; */
  /* width: 100%; */
  /* height: 100%; */
  position: fixed;
  /* background: #7f8c8d; */

  /* 最后使用的背景颜色 */
  /* background: rgba(11, 105, 160, 0.746); */
  /* z-index: -2; */
  /* 渐变色背景 */
  /* background: url(../img/content-background_2.jpg);
  background-size: 100% 100%;
  background-repeat: no-repeat; */
  /* 实现的渐变色背景_v1 */
  /* background: linear-gradient(135deg, #32607e8f 25%, #0ac29dbd 75%); */
  /* background: url('../img/other/background_1.jpg');
  background-size: cover; */
  /* 加入透明滤镜 */
  /* filter: opacity(60%); */

  height: 100%;
  overflow: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.my-top-navbar {
  position: absolute;
  top: 0px;
  width: 100%;
}
.container {
  margin-top: 0px;
}

.my-box {
  margin-top: 65px;
  display: flex;
  flex-direction: row;
  /* 注意需要加入wrap，因为flex-wrap的默认值是nowrap（不换行） */
  flex-flow: row wrap;
  justify-content: center;
}
.my-box > .my-row {
  flex: 0 0 25%;

  /* width: 250px; */
}
</style>