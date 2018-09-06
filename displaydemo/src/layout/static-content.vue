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
  import {
    getStaticUser,
    getLevel
  } from "../api/api.js";
  import {
    DepartmentMid,
    User
  } from "../common/model.js";
  // import {x} from "../api/api.js";
  import photoframe from "./photoframe.vue";

  export default {
    components: {
      photoframe
    },
    props: {
      nowDate: {
        type: Object,
        required: true
      }
    },
    methods: {
      //读取左侧的两个当日固定的领导值班员相关信息
      loadStaticPersonList: function () {
        var myself = this;

        // console.log("");
        var mid_model = new DepartmentMid(null, myself.nowDate.format('YYYY-MM-DD'));
        getStaticUser(mid_model).then(res => {
          // console.log(res);
          $.each(res.data, function (index, val) {
            var user_temp = new User(
              val.user.username,
              getLevel(val.user.level),
              val.rDepartmentDuty.duid.desc,
              val.rDepartmentDuty.did.derpartmentname,
              val.rDepartmentDuty.duid.dutyname,
              val.user.imgUrl
            );
            myself.vips.push(user_temp);
          });
          //对vip的顺序进行排序，让中心领导排到前面
          myself.vips = myself.vips.sort(myself.sortPerson);
        });
      },
      //对vip的排序算法
      sortPerson: function (a, b) {
        //注意此处，若是中心领导（urgency），则排在前面
        if (a.level === 'urgency') {
          return -1;
        } else {
          return 1;
        }
      }
    },
    data() {
      return {
        vips: [],
        selectedDate: ""
      };
    },
    compiled: () => {},
    // mounted: () => {},
    mounted: function () {
      var myself = this;

      //下面固定人员改为从后端读取
      // this.vips.push({
      //   level: "urgency",
      //   img_url: "./src/img/person/中心领导/易晓蕾.jpg",
      //   name: "易晓蕾",
      //   desc: "带班领导",
      //   other: "中心副主任"
      // });
      // this.vips.push({
      //   level: "minor",
      //   img_url: "./src/img/person/业务处/张志华.jpg",
      //   name: "张志华",
      //   desc: "应急管理值班岗",
      //   other: "业务处处长"
      // });
      this.loadStaticPersonList();
      // this.users.push({
      //     level: "norm",
      //     img_url: './src/img/person/预警室/傅赐福.jpg',
      //     name: '值班员D',
      //     desc: '风暴潮 警报班',
      //     group: '风暴潮',
      //     duty: '警报班'
      // });
    }
  };
</script>
<style scoped>
  .container {
    margin-top: 15px;
  }

  #left-content {
    left: 0px;
    top: 100px;
    /* margin-left: 0px;
        margin-top: 130px; */
    /* margin-bottom:0px; */
    width: 350px;
    height: 100%;
    position: fixed;
    z-index: 2;
    /* overflow: scroll; */
    /* background-color: rgba(3, 45, 184, 0.493); */
    /* background: rgba(73, 74, 95, 0.541); */
    background-color: rgb(249, 242, 187);
  }
</style>