$(function(){
	$(window).scroll(function(){
		if($(this).scrollTop()>=100){
			$("body").addClass("p-scrolling");
		}
		else{
			$("body").removeClass("p-scrolling");
		}
	});
	//菜单的下拉与收回
	$('.menu-btn').on('click',function(){
		$('.mm-menu').css('top','0%');
		$('.mm-top').css('top','0%');
		$('.mm-front').css('top','0%');
		$('.mm-next').css('top','0%');
		$('#header').css('display','none');
		$('.bannerPane').css('display','none');
		$('#menu').css('display','block');
	});
	$('.menu-btn2').on('click',function(){
		$('.mm-menu').css('top','-80%');
		$('.mm-top').css('top','-80%');
		$('.mm-front').css('top','-80%');
		$('.mm-next').css('top','-80%');
		$('#header').css('display','block');
		$('.bannerPane').css('display','block');
		$('#menu').css('display','none');
	});
	
	//获取后台数据
	var domain = "http://localhost:8000";
	var urlpath = window.location.pathname;
	var gender = urlpath.split('/')[2];
	if(gender!='0'){
		gender = 1;
	}
	$.getJSON(domain+'/candidates/gender/'+gender,function(data){
		$.each(data,function(index,item){
			for(attr in item){
				if(item[attr]==0)
					continue;
				if(item[attr]==null || item[attr]==undefined || item[attr]=="")
					delete item[attr];
			}
			item.parent='.o-team';
			$.profile(item);
		})
	});
	
	//加载列表
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
});
