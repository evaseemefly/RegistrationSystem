<template>
    <div>
        <div class="topcenterbar">
            <a href="#" v-on:click="onClick(index,obj)" :class="{'current':index===mark}" v-for="(obj,index) in departments" :key="index">{{obj.name}}</a>            
            <!-- <a href="#" class="current">预警室</a>
            <a href="#" class="current">环境室</a>
            <a href="#">海啸室</a> -->
        </div>
        <div class="topcontactbar">
          <div v-for="(obj,index) in contactList" :key="index">{{obj.derpartmentname}}|{{obj.phone}}</div>
        </div>
    </div>
</template>
<script>
import { getDepartmentList, getConactDepartmentList } from "../api/api.js";
import { Department } from "../common/model.js";
import bus from "../common/eventBus";
// import func from "./vue-temp/vue-editor-bridge.js";
export default {
  data() {
    return {
      departments: [],
      mark: 0,
      selected_department: {},
      // 当前选中的a标签
      currentIndex: 0,
      // 当前部门的联系人（组）列表
      contactList: []
      // 当前部门的一些信息
      // currentDepartment:{}
    };
  },
  watch: {
    // 监视当mark发生变化时，触发a标签的事件
    mark: function() {
      this.selected_department = this.departments[this.mark];
      // 触发点击事件
      this.onClick(this.mark, this.selected_department);
      this.loadUsers(this.selected_department);
      this.loadTargetDepartment(this.selected_department);
      this.loadContactDepartment(this.selected_department);
    }
  },
  methods: {
    //切换之后根据不同的部门id加载该部门该日的值班人员
    onClick: function(index, obj) {
      this.mark = index;
      console.log(index, obj);
      this.selected_department = obj;
    },
    //加载部门list
    loadDepartment: function() {
      var myself = this;
      var now_date = "2018-08-02";

      getDepartmentList().then(res => {
        $.each(res.data, function(index, val) {
          var department = new Department(
            val.pid,
            val.did,
            val.derpartmentname,
            val.phone
          );
          myself.departments.push(department);
        });
        // alert(res);
        //加载完部门后制定点击操作
        myself.onClick(0, myself.departments[0]);
      });
    },
    // 加载部门联系电话
    loadContactDepartment: function() {
      var myself = this;
      getConactDepartmentList(this.selected_department).then(res => {
        console.log(res);
        // 返回的res.data中是一个array
        myself.contactList = res.data;
      });
    },
    //加载指定部门的人员
    loadUsers: function(obj) {
      var myself = this;
      // bus.$emit("loadUserList",obj);
      // 调用父组件中的loadUserList方法并将选中的department传入
      this.$emit("loadUserList", obj);
    },
    loadTargetDepartment: function(obj) {
      var myself = this;

      this.$emit("loadDepartment", obj);
    },
    // a标签轮播
    autoPlay: function() {
      // 当前a标签索引加1
      this.mark++;

      var count_dep = this.departments.length;
      if (this.mark == count_dep) {
        this.mark = 0;
      }
    },
    toPaly: function() {
      // 暂时注释掉
      setInterval(this.autoPlay, 15000);
    }
  },
  mounted: function() {
    this.loadDepartment();
    // 测试时暂时去掉
    this.toPaly();
    //加入默认点击第一个a标签的操作
    // this.onClick(0,this.departments[0]);
  }
};
</script>
<style scoped>
.navbar-center {
  background-color: rgba(0, 57, 245, 0.089);
  margin-bottom: 2px;
}

.topcenterbar {
  text-align: center;
  height: 65px;
  color: rgb(213, 214, 226);
  font-weight: 500;
  font-family: "Microsoft YaHei", 宋体, "Segoe UI", "Lucida Grande", Helvetica,
    Arial, sans-serif, FreeSans, Arimo;
  background: rgba(73, 74, 95, 0.438);
}

.topcontactbar {
  text-align: center;
  height: 50px;
  color: rgb(213, 214, 226);
  font-weight: 500;
  font-family: "Microsoft YaHei", 宋体, "Segoe UI", "Lucida Grande", Helvetica,
    Arial, sans-serif, FreeSans, Arimo;
  background: rgba(138, 140, 181, 0.438);
  color: white;
  /*对于一行内容,直接设置Line-height与height相等即可*/
  line-height: 50px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.topcenterbar a {
  display: inline-block;
  margin: 0.5em;
  padding: 0.6em 1em;
  border: 3px solid #fff;
  font-weight: 700;
  color: #fff;
}

.topcenterbar a.current {
  background: #1d7db1;
  color: #fff;
}

/* a {
        color: aliceblue;
        font-size: large;
        font-weight: 300;
    } */
</style>