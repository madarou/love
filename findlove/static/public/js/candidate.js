$(function(){
	$(window).scroll(function(){
		if($(this).scrollTop()>=100){
			$("body").addClass("p-scrolling");
		}
		else{
			$("body").removeClass("p-scrolling");
		}
	});
	//从后台获取数据
	var domain = "http://localhost:8000";
	var id = getUrlParam('id');
	$.getJSON(domain+'/candidates/'+id,function(data){
		console.log(data);
		$('#uname').html((data.name)?data.name:'保密');
		$('#age').html((data.age)?data.age:'保密');
		$('#location').html((data.location)?data.location:'ta没说');
		$('#height').html((data.height)?data.height:'你猜');
		$('#weight').html((data.weight)?data.weight:'拿秤来');
		$('#college').html((data.college)?data.college:'不告诉你');
		$('#hometown').html((data.hometown)?data.hometown:'在哪遥远的地方');
		$('#constellation').html((data.constellation)?data.constellation:'你猜');
		$('#job').html((data.job)?data.job:'你再猜');
		$('#education').html((data.education)?data.education:'保密');
		$('#hobby').html((data.hobby)?data.hobby:'不能说的秘密');
	});
	var imglist = ["http://www.xipwang.cn/photoview/imgs/1.jpg","http://www.xipwang.cn/photoview/imgs/2.jpg",
	               "http://www.xipwang.cn/photoview/imgs/3.jpg","http://www.xipwang.cn/photoview/imgs/4.jpg",
	               "http://www.xipwang.cn/photoview/imgs/5.jpg","http://www.xipwang.cn/photoview/imgs/6.jpg",
	               "http://www.xipwang.cn/photoview/imgs/7.jpg"];
	$.gallery({parent:'#photos',imgs:imglist});//加载相片列表
	$("#PGalleryTwoC").photoview(); //生成图片预览模式
});
function getUrlParam(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
	var r = window.location.search.substr(1).match(reg); //匹配目标参数
	if (r != null) return unescape(r[2]);
	return null; //返回参数值
}