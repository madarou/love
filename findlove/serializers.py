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

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','name', 'description', 'avatar')
        
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