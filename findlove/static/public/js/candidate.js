$(function(){
	$(window).scroll(function(){
		if($(this).scrollTop()>=100){
			$("body").addClass("p-scrolling");
		}
		else{
			$("body").removeClass("p-scrolling");
		}
	});

	var imglist = ["http://www.xipwang.cn/photoview/imgs/1.jpg","http://www.xipwang.cn/photoview/imgs/2.jpg",
	               "http://www.xipwang.cn/photoview/imgs/3.jpg","http://www.xipwang.cn/photoview/imgs/4.jpg",
	               "http://www.xipwang.cn/photoview/imgs/5.jpg","http://www.xipwang.cn/photoview/imgs/6.jpg",
	               "http://www.xipwang.cn/photoview/imgs/7.jpg"];
	$.gallery({parent:'#photos',imgs:imglist});//加载相片列表
	$("#PGalleryTwoC").photoview(); //生成图片预览模式
})