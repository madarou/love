#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年9月13日

@author: makao
'''
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from findlove.serializers import UserSerializer, GroupSerializer, CandidateSerializer

from findlove.models import Snippet,Candidate
from findlove.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.core import serializers
from django.shortcuts import render_to_response

class CandidateList(APIView):
    """
    展示所有存在的Candidate, 或建立新的Candidate
    """
    #跳转页面的用法，还可以加入返回的数据
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'candidates.html'
    def get(self, request, format=None):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidateDetail(APIView):
    """
    展示, 更新或删除一个Candidate
    """
    def get_object(self, pk):
        try:
            return Candidate.objects.get(pk=pk)
        except Candidate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate)#有参数的Serializer类会在restore_object中实例化Candidate对象
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate, data=request.DATA)#这里会调用Serializer里的restore_object方法
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class SnippetList(APIView):
#     """
#     展示所有存在的snippet, 或建立新的snippet
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
# 
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# class SnippetDetail(APIView):
#     """
#     展示, 更新或删除一个snippet
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
# 
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
# 
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
def index(request,gender='boy'):
    #index=serializers.serialize("json", Index.objects.all())
    if gender != 'girl':
        gender = 'boy'
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR'] 
    #visitor = Visitor(ip=ip,time=datetime.datetime.now())
    #visitor.save()
    return render_to_response('candidates.html',{'gender':gender})