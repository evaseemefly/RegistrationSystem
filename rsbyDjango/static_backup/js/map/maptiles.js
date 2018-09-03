 var map = L.map('basemap').setView([25, 120], 4);
        mapLink = '~/data/mosic/';
        L.tileLayer(
            '../data/mosic/{z}/{x}/{y}.jpg', {
            attribution: '',
            maxZoom: 8,
			minZoom: 2			
            }).addTo(map);
  var status = 0;
  
  polygon.bindPopup("I am a polygon.");
	
  var popup = L.popup();

  //鼠标点击弹窗
  function onMapClick(e) {
      popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
  }  
  
  var poly_points = [];//区域
  var poly_line=new L.Polyline([]);//折线s
  
  
  
  //画矩形
  function addClickLatlng(e){
      //当前点
      var clickLocation=[e.latlng.lat,e.latlng.lng];
    poly_points.push(clickLocation);
    //显示折线
    poly_line.addLatLng(e.latlng);
    map.addLayer(poly_line);
      //var point=new L.Point(e.layerPoint.x,e.layerPoint.y);
  }
  
  //显示矩形
  function showPoly(){
      for (var i = 0, latlngs = [], len = poly_points.length; i < len; i++) {
      latlngs.push(new L.LatLng(poly_points[i][0], poly_points[i][1]));
      }
      var poly = new L.Polygon(latlngs);
      map.addLayer(poly);
      //清空
      poly_points=[];
      poly_line=new L.Polyline([]);
  }

   function onMouseMove(e){
	   var lat = e.latlng.lat.toFixed(4);
	   var lon = e.latlng.lng;
	   while(lon > 180)
	   {
		   lon = lon - 360;
	   }
	   while(lon < -180)
	   {
		   lon = lon + 360;
	   }
	   lon = lon.toFixed(4);
	  document.getElementById("latlon").innerHTML = "当前坐标：" + lat + ", " + lon;
	  
   }
   
   

	
