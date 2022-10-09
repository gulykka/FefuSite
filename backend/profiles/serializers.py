from rest_framework import serializers
from .models import *


# class PublicationModel:
#     def __init__(self, content):
#         self.content = content
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()

    class Meta:
        model = Publication
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
