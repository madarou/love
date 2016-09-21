$(function(){
	$(window).scroll(function(){
		if($(this).scrollTop()>=100){
			$("body").addClass("p-scrolling");
		}
		else{
			$("body").removeClass("p-scrolling");
		}
	});

	var imglist = ["/static/public/img/1-th.jpg","/static/public/img/2-th.jpg",
	               "/static/public/img/3-th.jpg","/static/public/img/4-th.jpg",
	               "/static/public/img/5-th.jpg","/static/public/img/1-th.jpg"];
	$.gallery({parent:'#photos',imgs:imglist});//加载相片列表
	$("#PGalleryTwoC").photoview(); //生成图片预览模式
})