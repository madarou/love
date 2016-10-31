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
		});
	});
	
	//加载列表
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
//	$.profile({parent:'.o-team'});
});
var data,
myScroll,
pullUpEl, pullUpOffset,
generatedCount = 0;


function pullUpAction () {

$.getJSON('/candidates/', function (data, state) {
	setTimeout(function () {
		$.each(data,function(index,item){
			for(attr in item){
				if(item[attr]==0)
					continue;
				if(item[attr]==null || item[attr]==undefined || item[attr]=="")
					delete item[attr];
			}
			item.parent='.o-team';
			$.profile(item);
		});
		myScroll.refresh();
	}, 600);
	/* if (data && data.state == 1 && state == 'success') {
		//本地测试，为了看到加载中效果故加上定时器
		setTimeout(function () {
			$('#news-lists').append(data.data);
			myScroll.refresh();
		}, 600);
	} */
});
}

//去除浏览器默认事件
document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);
//domready后绑定初始化事件
document.addEventListener('DOMContentLoaded', loaded, false);

function loaded() {
pullUpEl = document.getElementById('pullUp');	
pullUpOffset = pullUpEl.offsetHeight;

/**
 * 初始化iScroll控件
 */
myScroll = new iScroll('o-person-details-pane', {
	vScrollbar : false,
	onRefresh : function () {
		if (pullUpEl.className.match('loading')) {
			pullUpEl.className = '';
			pullUpEl.querySelector('.pullUpLabel').innerHTML = '上拉加载更多...';
		}
	},
	onScrollMove: function () {
		if (this.y < (this.maxScrollY - 5) && !pullUpEl.className.match('flip')) {
			pullUpEl.className = 'flip';
			pullUpEl.querySelector('.pullUpLabel').innerHTML = '松手开始更新...';
		}
	},
	onScrollEnd: function () {
		if (pullUpEl.className.match('flip')) {
			pullUpEl.className = 'loading';
			pullUpEl.querySelector('.pullUpLabel').innerHTML = '加载中...';				
			pullUpAction();
		}
	}
});
}
