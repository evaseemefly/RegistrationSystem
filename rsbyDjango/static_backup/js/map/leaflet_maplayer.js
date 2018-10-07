/**
 * Created by evase on 2017/9/29.
 */
var map;
map = L.map('leafletMap', {
    center: [30, 120],
    zoom: 4
});

// 影像
mapLink = '/static/img/mosic/';
L.tileLayer(
    '/static/img/mosic/{z}/{x}/{y}.jpg', {
        attribution: '',
        maxZoom: 8,
        minZoom: 2
    }).addTo(map);

// 边界
// L.tileLayer("http://t{s}.tianditu.cn/ibo_w/wmts?service=wmts&request=GetTile&version=1.0.0&LAYER=ibo&tileMatrixSet=w&TileMatrix={z}&TileRow={y}&TileCol={x}&style=default&format=tiles", {
// 	subdomains: ["0", "1", "2", "3", "4", "5", "6", "7"]
// }).addTo(map);



