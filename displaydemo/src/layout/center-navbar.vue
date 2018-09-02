<template>
    <div>
        <div class="topcenterbar">
            <a href="#" v-on:click="onClick(index,obj)" :class="{'current':index===mark}" v-for="(obj,index) in departments" :key="index">{{obj.name}}</a>
            <!-- <a href="#" class="current">预警室</a>
            <a href="#" class="current">环境室</a>
            <a href="#">海啸室</a> -->
        </div>
    </div>
</template>
<script>
import { getDepartmentList } from "../api/api.js";
import { Department } from "../common/model.js";
import bus from "../common/eventBus";
export default {
  data() {
    return {
      departments: [],
      mark: 0,
      selected_department: {}
    };
  },
  methods: {
    //切换之后根据不同的部门id加载该部门该日的值班人员
    onClick: function(index, obj) {
      this.mark = index;
      console.log(index, obj);
      this.selected_department = obj;
      this.loadUsers(obj);
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
            val.derpartmentname
          );
          myself.departments.push(department);
        });
        // alert(res);
      });
    },
    //加载指定部门的人员
    loadUsers: function(obj) {
      var myself = this;
      // bus.$emit("loadUserList",obj);
      // 调用父组件中的loadUserList方法并将选中的department传入
      this.$emit("loadUserList", obj);
    }
  },
  mounted: function() {
    this.loadDepartment();
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