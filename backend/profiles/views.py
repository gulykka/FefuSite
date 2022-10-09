from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import *


class ProfileApi(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class PublicationApi(APIView):

    def get(self, request):
        publications = Publication.objects.all()
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)

    def post(self, request):
        publication = PublicationSerializer(data=request.data)
        if publication.is_valid():
            publication.save(user=request.user)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class BuildingsApi(APIView):

    def get(self, request):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
