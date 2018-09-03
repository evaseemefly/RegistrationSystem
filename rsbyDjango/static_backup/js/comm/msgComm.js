/**
 * Created by evase on 2017/10/24.
 */

function loaderrmsg(id_title,id_msg,title,msg){
    //加载指定
    // document.getElementById("#"+id_title).innerHTML = title;
    // document.getElementById("#"+id_msg).innerHTML = msg;

    document.getElementById(id_title).innerHTML = title;
    document.getElementById(id_msg).innerHTML = msg;
	$("#errorModal").modal();
}