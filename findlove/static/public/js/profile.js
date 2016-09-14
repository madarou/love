//一个profile就是列表中的一项，包含了用户头像，签名，职业，所在地，等等信息的展示
;(function($,window,undifined){
	var Profile = function(options){
		this.settings=$.extend({},Profile.defaults,options);
		this.init();
	}
	
	Profile.prototype={
			//初始化
			init:function(){
				this.create();
			},
			//创建，主要创建html元素和css
			create:function(){
				var template ='<div class="about-img">'+
									'<img src="'+this.settings.avatar+'" />'+
								'</div>'+
								'<div class="about-sDetails">'+
									'<h3>'+this.settings.name+'</h3>'+
									'<h4>'+this.settings.job+'</h4>'+
								'</div>'+
								'<div class="about-openBtn">'+
									'<i class="fa fa-plus"></i>'+
								'</div>'+
								'<div class="o-person-content">'+this.settings.detail+
								'</div>';
				this.profile=$('<div>').addClass('o-team-person').html(template).appendTo(this.settings.parent);
				this.toggle();
			},
			//添加展开与折叠功能
			toggle:function(){
				var openBtn = this.profile.find('.about-openBtn');
				var _that = this;
				openBtn.on('click',function(){
					var self = $(this);
					if(self.hasClass("active"))
					{
						_that.profile.find(".o-person-content").slideUp(500);
						self.removeClass("active").find('i').removeClass("fa-minus");
						return false;
					}
					self.addClass("active").find('i').addClass("fa-minus");
					_that.profile.find(".o-person-content").slideDown(500);
					//$("body.o-page").animate({ scrollTop: self.parent().offset().top -80 }, 600);
				})
			}
	}
	
	Profile.defaults={
			name:'无名氏',
			description:'寻找爱',
			avatar:'/static/public/img/logo.jpg',
			job:'工程师',
			detail:'没有更多...',
			parent:'body'//父元素，以#xxx的id形式传入
	}
	var profile=function(options){
		return new Profile(options);
	}
	window.profile = $.profile = profile;
})(window.JQuery||window.Zepto,window);