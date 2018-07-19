import Vue from 'vue'
import App from './app.vue'
import $ from 'jquery'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'


import moment from 'moment'

Vue.prototype.moment=moment
Vue.config.devtools=true;
// Vue.use(VueRouter)
const root=document.createElement("div")
document.body.appendChild(root)

new Vue({
    //使用箭头语法等同于下面的写法
    render:(h)=>h(App)
}).$mount(root)     //$mount为vue中的手动挂载
console.log(process.env.NODE_ENV)