<template>
  <div id="content">
    <centernavbar class="my-top-navbar" @loadUserList="loadUserList"></centernavbar>
    <div class="container my-box">
      <div class="col-md-4 my-row" v-for="user in users">
        <photoframe v-bind:person=user></photoframe>
      </div>

    </div>
  </div>
</template>
<script>
import { getUserListByDepartment, getLevel } from '../api/api.js'
import { DepartmentMid, User } from '../common/model.js'
import photoframe from './photoframe.vue'
import centernavbar from './center-navbar.vue'
export default {
	components: {
		photoframe,
		centernavbar,
	},
	data() {
		return {
			users: [],
			selected_date: '',
		}
	},
	methods: {
		//加载userlist
		loadUserList: function(params) {
			var myself = this

			//为当前时间赋值
			myself.selected_date = '2018-08-02'
			myself.users = []
			var mid_model = new DepartmentMid(params.did, myself.selected_date)
			getUserListByDepartment(mid_model).then(res => {
				// console.log(res)
				$.each(res.data, function(index, val) {
					var user_temp = new User(
						val.user.username,
						getLevel(val.user.level),
						val.rDepartmentDuty.duid.desc,
						val.rDepartmentDuty.did.derpartmentname,
						val.rDepartmentDuty.duid.dutyname,
						val.user.imgUrl
					)
					myself.users.push(user_temp)
				})
			})
		},
	},
	mounted: function() {
		// this.users.push({
		// 	level: 'import',
		// 	img_url: './src/img/person/预警室/董剑希.jpg',
		// 	name: '董剑希',
		// 	desc: '带班主任',
		// 	group: '室主任',
		// 	duty: '带班主任',
		// })
		// this.users.push({
		// 	level: 'import',
		// 	img_url: './src/img/person/环境室/李云.jpg',
		// 	name: '李云',
		// 	desc: '带班主任',
		// 	group: '室主任',
		// 	duty: '带班主任',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/预警室/侯放.jpg',
		// 	name: '侯放',
		// 	desc: '风暴潮 主班',
		// 	group: '风暴潮',
		// 	duty: '主班',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/预警室/梁森栋.jpg',
		// 	name: '梁森栋',
		// 	desc: '风暴潮 副班',
		// 	group: '风暴潮',
		// 	duty: '副班',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/预警室/徐瑞.jpg',
		// 	name: '徐瑞',
		// 	desc: '风暴潮 24小时岗',
		// 	group: '风暴潮',
		// 	duty: '24小时岗',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/预警室/傅赐福.jpg',
		// 	name: '傅赐福',
		// 	desc: '风暴潮 警报班',
		// 	group: '风暴潮',
		// 	duty: '警报班',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/环境室/于寒.jpg',
		// 	name: '于寒',
		// 	desc: '环境 24小时',
		// 	group: '环境',
		// 	duty: '24小时岗',
		// })
		// this.users.push({
		// 	level: 'norm',
		// 	img_url: './src/img/person/环境室/李志杰.jpg',
		// 	name: '李志杰',
		// 	desc: '环境 主班',
		// 	group: '环境',
		// 	duty: '主班',
		// })
	},
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
	display: flex;
	flex-direction: row;
	justify-content: center;
}
.my-box > .my-row {
	/* width: 250px; */
}
</style>