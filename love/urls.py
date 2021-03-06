"""love URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from findlove import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
    
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),
    #url(r'^login/$', views.LoginViewSet.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^candidates/$', views.CandidateList.as_view()),
    url(r'^candidates/(?P<pk>[0-9]+)/$', views.CandidateDetail.as_view()),
    
    url(r'^candidate/manage/(?P<pk>[0-9]+)/$', views.CandidateManage.as_view(),name="manage"),
    url(r'^candidates/manage/$', views.CandidatesManage.as_view(),name="manages"),
    url(r'^candidate/add/$', views.CandidatesAdd.as_view(),name="add"),
    
    url(r'^candidates/gender/$', views.GenderList.as_view()),
    url(r'^candidates/gender/(?P<gender>[0-9]+)/$', views.GenderList.as_view()),
    url(r'^$',views.index,name='index'),
    url(r'^index/$', views.index,name='index'),
    url(r'^index/(?P<gender>[0-9]*)/$', views.index,name='index'),
    url(r'^templates/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'findlove/templates', 'show_indexes': True}),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)