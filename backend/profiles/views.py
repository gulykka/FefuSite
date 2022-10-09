# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import generics
# from rest_framework.response import Response
#
# from .models import Publication, Category
# from .serializers import PublicationSerializer
# from rest_framework.views import APIView
#
#
# def index(request):
#     publications = Publication.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'publications': publications,
#         'author': 'Публикации',
#         'categories': categories,
#     }
#     return render(request, 'profiles/index.html', context=context)
#
#
# def get_category(request, category_id):
#     publications = Publication.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'profiles/category.html', {'publications': publications, 'categories': categories,
#                                                       'category': category})
#
#
# # class PublicationAPIView(generics.ListAPIView):
# #     queryset = Publication.objects.all()
# #     serializer_class = PublicationSerializer
#
# class PublicationAPIView(APIView):
#     def get(self, request):
#         lst = Publication.objects.all()
#         return Response({'publication': PublicationSerializer(lst, many=True).data})
#
#     def post(self, request):
#         return Response({'title': 'How are you doing&'})

from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework import generics


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]


class PublicationsList(generics.ListAPIView):
    queryset = Publication.objects.order_by('id')
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]
