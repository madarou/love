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
				if(this.settings.gender==0)
					this.settings.avatar='/findlove/static/public/img/avatar/girl.jpg';
				//构造模板
				var template ='<div class="about-img">'+
									'<img src="'+this.settings.avatar.substr(9)+'" />'+
								'</div>'+
								'<a  style="text-decoration:initial" href="'+this.settings.href+'?id='+this.settings.id+'"><div class="about-sDetails">'+
									'<h3>'+this.settings.name+'</h3>'+
									'<h4>'+this.settings.age+'&nbsp;'+this.settings.location+'</h4>'+
									'<h4>'+this.settings.description+'</h4>'+
								'</div></a>'+
								'<div class="about-openBtn">'+
									'<i class="fa fa-plus"></i>'+
								'</div>'+
								'<a  style="text-decoration:initial" href="'+this.settings.href+'?id='+this.settings.id+'"><div class="o-person-content">'+this.settings.intro+
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
				var innerContent = "";
				if(this.settings.job!='')
					innerContent += '<a class="o-buttons red"><i class="fa fa-suitcase"></i> '+this.settings.job+'</a>';
				if(this.settings.constellation!='')
					innerContent += '<a class="o-buttons red"><i class="fa fa-star"></i> '+this.settings.constellation+'</a>';
				if(this.settings.height!='')
					innerContent += '<a class="o-buttons red"><i class="fa fa-male"></i> '+this.settings.height+'</a>';
				if(this.settings.weight!='')
					innerContent+= '<a class="o-buttons red"><i class="fa fa-balance-scale"></i> '+this.settings.weight+'</a>';
				if(this.settings.hometown!='')
					innerContent += '<a class="o-buttons red"><i class="fa fa-home"></i> '+this.settings.hometown+'人</a>';
				if(this.settings.college!='')
					innerContent += '<a class="o-buttons red"><i class="fa fa-university"></i> '+this.settings.college+'</a>';
				if(this.settings.education!='')
					innerContent+= '<a class="o-buttons red"><i class="fa fa-mortar-board"></i> '+this.settings.education+'</a>';
				if(this.settings.hobby!='')
					innerContent+= '<a class="o-buttons red"><i class="fa fa-soccer-ball-o"></i> '+this.settings.hobby+'</a>';
				if(innerContent!="")
					container.html(innerContent);
				else
					container.html('<a class="o-buttons red"><i class="fa fa-user-secret"></i>Ta比较害羞，没写标签</a>');
			}
	}
	
	Profile.defaults={
			id:0,//id，作为参数传到下一页面
			name:'马秋田',
			gender:1,
			description:'Ta没说话，只是静静地等待...',
			avatar:'/findlove/static/public/img/avatar/boy.jpg',
			job:'',
			age:'25',
			location:'上海浦东',
			constellation:'',
			height:'',
			weight:'',
			hometown:'',
			college:'',
			education:'',
			hobby:'',
			intro:'没有更多...<br/>没有更多...<br/>没有更多...<br/>没有更多...<br/>',
			href:'/templates/candidate.html',//点击后指向的页面地址
			parent:'body'//父元素，以#xxx的id形式传入
	}
	var profile=function(options){
		return new Profile(options);
	}
	window.profile = $.profile = profile;
})(window.JQuery||window.Zepto,window);