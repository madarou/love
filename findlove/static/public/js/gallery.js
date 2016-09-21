;(function($,window,undefined){
	var Gallery = function(options){
		this.settings=$.extend({},Gallery.defaults,options);
		this.settings=$.extend({},this.settings,{number:this.settings.imgs.length});
		this.init();
	}
	
	Gallery.prototype={
			init:function(){
				this.create();
			},
			//创建元素html和css框架
			create:function(){
				var template = '<div class="gallery-row">'+
									'<div id="PGalleryTwoC" class="row">'+
									'</div>'+
								'</div>';
				this.gallery=$('<div>').addClass('gallery').html(template).appendTo(this.settings.parent);
				this.fillData();
			},
			fillData:function(){
				var container = this.gallery.find('#PGalleryTwoC');
				var col1 = $('<div>').addClass('mobile-two');
				var firsthalf = Math.ceil(this.settings.number/2);
				var items = "";
				for(var i=0;i<firsthalf;i++){
					items += '<div class="gallery-item"><a rel="external"><img src="'+this.settings.imgs[i]+'"></a></div>';
				}
				col1.html(items);
				var col2 = $('<div>').addClass('mobile-two');
				items = "";
				for(var j=firsthalf;j<this.settings.number;j++){
					items += '<div class="gallery-item"><a rel="external"><img src="'+this.settings.imgs[j]+'"></a></div>';
				}
				col2.html(items);
				col1.appendTo(container);
				col2.appendTo(container);
			}
	}
	
	Gallery.defaults={
			parent:'body',//父元素，gallery要插入到的地方
			imgs:null//需要显示的图片url列表
	}
	
	var gallery=function(options){
		return new Gallery(options);
	}
	window.gallery = $.gallery = gallery;
})(window.JQuery||window.Zepto, window);