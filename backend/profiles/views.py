from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework import generics
from .models import *


class ProfileApi(generics.ListCreateAPIView):
    queryset = Profile.objects.order_by('id')
    serializer_class = SpecialUserSerializer
    permission_classes = [AllowAny]


class PublicationApi(generics.ListCreateAPIView):
    queryset = Publication.objects.order_by('id')
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]


class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]


class CategoryApi(generics.ListAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class BuildingsList(generics.ListAPIView):
    queryset = Building.objects.order_by('id')
    serializer_class = BuildingSerializer
    permission_classes = [AllowAny]
