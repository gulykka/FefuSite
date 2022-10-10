from rest_framework import serializers
from .models import *


# class PublicationModel:
#     def __init__(self, content):
#         self.content = content
class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'phone_number', 'name', 'building', 'last_login')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'building']


class PublicationSerializer(serializers.ModelSerializer):
    author = SpecialUserSerializer()

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
