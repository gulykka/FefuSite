from rest_framework import serializers
from .models import *


# class PublicationModel:
#     def __init__(self, content):
#         self.content = content
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'number',)


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('author', 'content', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
