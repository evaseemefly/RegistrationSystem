/**
 * Created by evase on 2017/9/29.
 */

//使用ko的方式进行绑定，使用js的方式声明对象
function RectangleMeasureViewModel() {
    var self = this;
    self.startPoint = null;
    self.endPoint = null;
    self.rectangle = null;
    self.tips = null;
    self.layer = L.layerGroup();

     // self.targetdate=ko.observable(0);
    self.startlat = ko.observable(0);
    self.startlng = ko.observable(0);
    self.finishlat = ko.observable(0);
    self.finishlng = ko.observable(0);
    self.formattedStartLat=ko.computed({
        read:function(){
            return formattedLatLng(self.startlat());
        },
        write:function(value){
            value=isNaN(value)?0:value;
            self.startlat(value);
        },
//					owner:this
    });
    self.formattedFinishLat=ko.computed({
        read:function(){
            return formattedLatLng(self.finishlat());
        },
        write:function(value){
            value=isNaN(value)?0:value;
            self.finishlat(value);
        },
//					owner:this
    });
    self.formattedStartLng=ko.computed({
        read:function(){
            return formattedLatLng(self.startlng());
        },
        write:function(value){
            value=isNaN(value)?0:value;
            self.startlng(value);
        },
//					owner:this
    });
    self.formattedFinishLng=ko.computed({
        read:function(){
            return formattedLatLng(self.finishlng());
        },
        write:function(value){
            value=isNaN(value)?0:value;
            self.finishlng(value);
        },
//					owner:this
    });

    self.getData=function () {
        var data={
            startlat:self.formattedStartLat(),
            startlng:self.formattedStartLng(),
            finishlat:self.formattedFinishLat(),
            finishlng:self.formattedFinishLng()
        }
        return data;
    }
    self.color = "#B92C28";
    self.isDrawing=ko.observable(false);
    self.addRectangle = function() {
        self.destory();
        var bounds = [];
        bounds.push(self.startPoint);
        bounds.push(self.endPoint);
        self.rectangle = L.rectangle(bounds, {
            color: self.color,
            weight: 1
        });
        self.rectangle.addTo(self.layer);

        var northWestPoint = self.rectangle.getBounds().getNorthWest(),
            northEastPoint = self.rectangle.getBounds().getNorthEast(),
            southEastPoint = self.rectangle.getBounds().getSouthEast();
        var width = northWestPoint.distanceTo(northEastPoint) / 1000,
            height = northEastPoint.distanceTo(southEastPoint) / 1000;
        self.layer.addTo(map);
    };
    self.addTips = function(area) {
        console.log('面积:' + area);
        self.tips = L.circleMarker(self.endPoint, {
            color: self.color
        });
        self.tips.setRadius(1);
        //rectangleMeasure.tips.bindLabel("面积：" + area + "(平方公里)", {noHide: true, direction: 'right', clickable: true, className: "leaflet-label-tffq"});
        self.tips.addTo(self.layer);
    };
    self.mousedown = function(e) {
        if(self.isDrawing==true){
            self.clearRectangle();
            return;
        }
        self.isDrawing=true;
        self.rectangle = null;
        self.tips = null;
        //map.dragging=false;
        map.dragging.disable();
        self.startPoint = e.latlng;
        self.startlat(self.startPoint["lat"]);
        self.startlng(self.startPoint["lng"]);
        map.on('mousemove', self.mousemove)
    };
    self.mousemove = function(e) {
        self.endPoint = e.latlng;
        self.finishlat(self.endPoint["lat"]);
        self.finishlng(self.endPoint["lng"]);
        self.addRectangle();
        //关闭关于mousedown的监听
        //开启对mouseup的监听
        map.off('mousedown ', self.mousedown).on('mouseup', self.mouseup);
    };
    self.mouseup = function(e) {
        self.close();
        //地图设置为可拖拽的
        //map.dragging=true;
        map.dragging.enable();
        map.off('mousemove', self.mousemove).off('mouseup', self.mouseup).off('mousedown', self.mousedown);
    };
    self.destory = function() {
        if(self.rectangle)
            self.layer.removeLayer(self.rectangle);
        if(self.tips)
            self.layer.removeLayer(self.tips);
    };
    self.close = function() {

    }
    //鼠标点击右键时执行
    //1、关闭框选操作；2、鼠标可以漫游
    self.forbidRegion = function(e) {
        alert("点击鼠标右键");
        self.clearRectangle();
//					self.rectangle.remove();

    }
    //清除当前的矩形
    self.clearRectangle=function(){
        self.isDrawing=false;
        self.rectangle.remove();
    }
}

function formattedLatLng(value){
    //保留两位有效数字
    if(value==undefined){
        return 0;
    }
    else
        var result=parseFloat(value).toFixed(2);
        return result;

}