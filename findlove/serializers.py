#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年9月13日

@author: makao
'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from findlove.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Candidate
from django.forms.fields import ImageField

class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=False, max_length=1024)
    password = serializers.CharField(required=False, max_length=1024)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        
class CandidateSerializer(serializers.ModelSerializer):
    avatar=ImageField(max_length=None, allow_empty_file=False)
    header=ImageField(max_length=None, allow_empty_file=False)
    photo1=ImageField(max_length=None, allow_empty_file=False)
    photo2=ImageField(max_length=None, allow_empty_file=False)
    photo3=ImageField(max_length=None, allow_empty_file=False)
    photo4=ImageField(max_length=None, allow_empty_file=False)
    photo5=ImageField(max_length=None, allow_empty_file=False)
    photo6=ImageField(max_length=None, allow_empty_file=False)
    photo7=ImageField(max_length=None, allow_empty_file=False)
    photo8=ImageField(max_length=None, allow_empty_file=False)
    photo9=ImageField(max_length=None, allow_empty_file=False)
    photo10=ImageField(max_length=None, allow_empty_file=False)
    detail = serializers.CharField(
        allow_blank=True,
        max_length=4000,
        style={'base_template': 'textarea.html', 'rows': 20}
    )
    class Meta:
        model = Candidate
        fields = ('id','name','gender','avatar','age','location','description','job','constellation',
                 'height', 'weight','hometown','education','college','hobby','header','detail','photo1',
                 'photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10','pubtime')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()  # `Field` 是无类型, 只读的.
    title = serializers.CharField(required=False,
                                  max_length=100)
    code = serializers.CharField(required=False,
                                 max_length=100)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
                                       default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,
                                    default='friendly')

    def restore_object(self, attrs, instance=None):
        """
        创建或更新一个snippet实例, 返回该snippet实例

        如果不定义该function, 则反序列化时将返回一个包括所有field的dict
        """
        if instance:
            # 更新已存在的snippet实例
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        return Snippet(**attrs)

