<template>
    <div>
			<div class="phoneframe">
				<div class="phone-department">{{department.name}}</div>
				<div class="phone-content">电话</div>
				<h2 class="phone">{{department.phone}}</h2>
			</div>
		</div>
</template>

<script>
export default {
  props: {
    department: {
      type: Object,
      required: true
    }
  }
};
</script>

<style>
.phoneframe {
  /* 外面阴影 */
  box-shadow: 0 0 30px #666666;
  position: absolute;
  top: 80px;
  left: 100px;
  height: 80px;
  width: 150px;
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  /*align-content: center;*/
  background: whitesmoke;
  border-radius: 0.8em;
  overflow: hidden;
}

.phoneframe > .phone-department {
  height: 30px;
  width: 100px;
  background: #e74c3c;
  color: #ffffff;
  /*justify-content: center;
				align-items: center;*/
  vertical-align: middle;
  line-height: 30px;
  text-align: center;
}
.phoneframe > .phone-content {
  /*width: 50px;*/
  height: 30px;
  flex-grow: 1;
  background: #d16f1f;
  color: #ffffff;
  /*justify-content: center;
				align-items: center;*/
  /*注意下面这种方式只对行内元素有效,对快内元素无效!!注意*/
  /*vertical-align: middle;*/
  line-height: 30px;
  text-align: center;
  display: table-cell;
}
</style>
