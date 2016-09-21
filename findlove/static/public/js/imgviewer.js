;(function($,wd,dc){
	$.fn.photoview=function(){
		function  PhotoView (element,options){
				this.elemnt=element
				this.arr =this.elemnt.children();
				this.bodyNode = $(document.body);
				this.winW = $(window).width()
				this.winH = $(window).height();												
				this.init();
		};

		PhotoView.prototype = {
			init:function(){
			     var m = this;
			     m.index = 0;
			     m.scale = m.winW/m.winH;
//			     m.mask  = $('<div class="mask-v-box">').css('height',$(wd).height()).css('top',$(wd).scrollTop()+$(wd).height()*2);
//			     m.wrap  = $('<div class="wrapView-v">').css('height',$(wd).height()).css('top',$(wd).scrollTop()+$(wd).height()*2);
			     m.mask  = $('<div class="mask-v-box">').css('height',$(wd).height());
			     m.wrap  = $('<div class="wrapView-v">').css('height',$(wd).height());
			     m.ulbox = $('<ul class="list-photo">');
			     m.pageindex = $('<span class="page-view">×');											
				 m.eventShow(m);
				 m.slideEvent(m);
			},	
			getDates:function(m){	
				var	arrurl=[];
				var arrImg=[];
				m.arr.each(function(i,v){ 
					var url=$(this).find('img').attr('src');
					arrurl.push(url);
					arrImg.push(new Image());
				});
				return{
					arrurl:arrurl,
					arrImg:arrImg
				};
			},
			createdom:function(m){  
				var  img =m.getDates(m).arrImg;
				var  url =m.getDates(m).arrurl;								
				m.bodyNode.append(m.mask).append(m.wrap);								
				m.wrap.append(m.ulbox).append( m.pageindex);
				for(var i=0; i<img.length;i++){			
						img[i].src=url[i];									
						if(img[i].width/img[i].height > m.scale){ 
							m.ulbox.append('<li>'+'<img src='+url[i]+' width="100%">'+'</li>');					
						}else{
							m.ulbox.append('<li>'+'<img src='+url[i]+' height="100%">'+'</li>');
						};
						m.ulbox.width(m.winW*img.length).height(m.winH);						
						m.ulbox.children().width(m.winW).height(m.winH);		
				   };
				m.mask.hide();
				m.wrap.hide();   
			 },
			 slideEvent:function(m){
		 		m.ulbox.swipeLeft(function(e){ 
		 			m.index++;
		 			e.preventDefault();		 			
		 			m.movephoto(m,m.index);
		 		});
		 		m.ulbox.swipeRight(function(e){
		 			m.index--;
		 			e.preventDefault();
		 			m.movephoto(m,m.index);
		 		});
			 },
			 Edefault:function(bool){
				document.ontouchstart=function(){
					return bool;
				}
			 },
			 eventShow:function(m){
		 		m.arr.on("tap",function(e){
		 			e.stopPropagation();
		 			 m.index=$(this).index();	
		 			 m.createdom(m);
					 m.Edefault(false);								 		
		 			 m.movephoto(m,m.index);
		 			 m.mask.show();
					 m.wrap.show();  						 			
		 			 m.wrap.on("tap",function(){
	 				          m.Edefault(true);	
	 					 m.wrap.remove();
	 					 m.mask.remove();
		 			});							 		
		 		});
			 },
			 movephoto:function(m,index){
			 	if(index >m.getDates(m).arrImg.length-1){
		 			index =m.index= m.getDates(m).arrImg.length-1;
		 		  }
		 		if(index  <0){
		 			index =m.index =0;
		 		};
		 		  m.pageindex.text(index+1+'/'+m.arr.length)
			 	  m.ulbox.css("-webkit-transform","translateX(-"+index* m.winW+"px)"); 
			 },
	  	};
		return this.each(function(){
				new  PhotoView($(this));
		});
  };
})(Zepto,window,document);