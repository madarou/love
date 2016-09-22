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
from django.core import serializers
from django.shortcuts import render_to_response, redirect
import datetime

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import FormParser, MultiPartParser

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
        serializer = SnippetSerializer(data=request.data)
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
        serializer = CandidateSerializer(candidate, data=request.data)#这里会调用Serializer里的restore_object方法
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenderList(APIView):
    """
    根据性别返回list
    """
    #跳转页面的用法，还可以加入返回的数据
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'candidates.html'
    def get(self, request, gender, format=None):
        gender=int(gender.encode('ascii'))
        if gender != 0:#这里从url取得的gender是Unicode的，需要转码才能跟0比较
            gender = 1
        candidates = Candidate.objects.filter(gender=gender).order_by('-pubtime')
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

class CandidateManage(APIView):
    '''
    后台修改candidate
    '''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'candidate_manage.html'

    parser_classes = (FormParser,MultiPartParser)
    def get(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response({'serializer': serializer, 'candidate': candidate})

    def post(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        request.data.update({'pubtime':datetime.datetime.now()})
        #如果没上传图片，则图片值不变
        #if request.data['avatar'] == '':
        #    request.data.update({'avatar':candidate.avatar})
        self.keepFields(request.data, candidate)
        serializer = CandidateSerializer(candidate, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'candidate': candidate})
        serializer.save()
        return redirect('manages')
    
    def keepFields(self, dict, old):
        '''如果request传来的值的key的value是空，则用原来的数据库里的值来填充它
            防止ImageField这些在上次传了这次没传后其值被更新成了空
        '''
        for key, value in dict.items():
            if value == '' or value is None:
                dict.update({key:getattr(old,key)})#
class CandidatesManage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'candidate_list.html'

    def get(self, request):
        candidates = Candidate.objects.all()
        #return Response(serializer.data)
        return Response({'candidates': candidates})
    
class CandidatesAdd(APIView):
    '''增加candidate'''
    '''
    后台添加candidate
    '''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'candidate_add.html'

    parser_classes = (FormParser,MultiPartParser)
    def get(self, request):
        #candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(None)
        return Response({'serializer': serializer})

    def post(self, request):
        request.data.update({'pubtime':datetime.datetime.now()})
        serializer = CandidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('manages')

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
    
def index(request,gender=1):
    #index=serializers.serialize("json", Index.objects.all())
    if gender != 0:
        gender = 1
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR'] 
    #visitor = Visitor(ip=ip,time=datetime.datetime.now())
    #visitor.save()
    return render_to_response('candidates.html',{'gender':gender})


