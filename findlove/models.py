#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年9月13日

@author: makao
'''
from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import datetime
import json
from love import settings

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class BaseModel(models.Model):
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
    
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr),models.Model):
                #d[attr] = serializers.serialize("json", [getattr(self, attr)])跳过外键关联的Model的序列化
                pass
            else:
                d[attr] = getattr(self, attr)
          
        return json.dumps(d)
    class Meta:
            abstract = True
            
class Candidate(BaseModel):
    name=models.CharField(max_length=30,null=True)
    gender=models.PositiveSmallIntegerField(default=1)
    avatar=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/avatar/',null=True)#列表小头像
    age=models.IntegerField(null=True)
    location=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=255,null=True)#个人签名，或择偶要求，或爱情宣言，简短的列表展示
    job=models.CharField(max_length=30,null=True)
    constellation=models.CharField(max_length=10,null=True)
    height=models.CharField(max_length=10,null=True)
    weight=models.CharField(max_length=10,null=True)
    hometown=models.CharField(max_length=50,null=True)
    education=models.CharField(max_length=30,null=True)
    college=models.CharField(max_length=50,null=True)
    hobby=models.CharField(max_length=50,null=True)
    header=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/header/',null=True)#个人展示的大头像
    detail=models.TextField(null=True)
    photo1=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo2=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo3=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo4=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo5=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo6=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo7=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo8=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo9=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    photo10=models.ImageField(upload_to=settings.STATIC_FILE_PATH+'/img/photos/',null=True)
    pubtime=models.DateTimeField(null=True)#发布时间
    
    
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)

    class Meta:
        ordering = ('created',)#指返回的结果按created字段升序排列