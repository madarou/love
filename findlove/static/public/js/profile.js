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
				//构造模板
				var template ='<div class="about-img">'+
									'<img src="'+this.settings.avatar+'" />'+
								'</div>'+
								'<a  style="text-decoration:initial" href="'+this.settings.href+'?id='+this.settings.id+'"><div class="about-sDetails">'+
									'<h3>'+this.settings.name+'</h3>'+
									'<h4>'+this.settings.age+'&nbsp;'+this.settings.location+'</h4>'+
									'<h4>'+this.settings.description+'</h4>'+
								'</div></a>'+
								'<div class="about-openBtn">'+
									'<i class="fa fa-plus"></i>'+
								'</div>'+
								'<a  style="text-decoration:initial" href="'+this.settings.href+'?id='+this.settings.id+'"><div class="o-person-content">'+this.settings.detail+
								'</div></a>';
				//加入父页面
				this.profile=$('<div>').addClass('o-team-person').html(template).appendTo(this.settings.parent);
				//增加自定义行为
				this.toggle();
				//添加detail内容
				this.detail();
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
			},
			//为profile添加
			detail:function(){
				var container = this.profile.find('.o-person-content');
				var job = '<a class="o-buttons red"><i class="fa fa-suitcase"></i> '+this.settings.job+'</a>';
				var constellation = '<a class="o-buttons red"><i class="fa fa-star"></i> '+this.settings.constellation+'</a>';
				var height = '<a class="o-buttons red"><i class="fa fa-male"></i> '+this.settings.height+'</a>';
				var hometown = '<a class="o-buttons red"><i class="fa fa-home"></i> '+this.settings.hometown+'人</a>';
				var college = '<a class="o-buttons red"><i class="fa fa-university"></i> '+this.settings.college+'</a>';
				var education = '<a class="o-buttons red"><i class="fa fa-mortar-board"></i> '+this.settings.education+'</a>';
				var hobby = '<a class="o-buttons red"><i class="fa fa-smile-o"></i> '+this.settings.hobby+'</a>';
				container.html(job+constellation+height+hometown+college+education+hobby);
			}
	}
	
	Profile.defaults={
			name:'马秋田',
			description:'寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱寻找爱',
			avatar:'/static/public/img/logo.jpg',
			job:'工程师',
			age:'25',
			location:'上海浦东',
			constellation:'射手座',
			height:'170cm',
			hometown:'河北石家庄',
			college:'蓝翔技校',
			education:'硕士',
			hobby:'足球,篮球',
			detail:'没有更多...<br/>没有更多...<br/>没有更多...<br/>没有更多...<br/>',
			href:'/templates/candidate.html',//点击后指向的页面地址
			id:1,//id，作为参数传到下一页面
			parent:'body'//父元素，以#xxx的id形式传入
	}
	var profile=function(options){
		return new Profile(options);
	}
	window.profile = $.profile = profile;
})(window.JQuery||window.Zepto,window);