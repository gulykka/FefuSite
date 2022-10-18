from rest_framework import serializers
from .models import *


class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'phone_number', 'name', 'building', 'last_login')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'building']


class PublicationSerializer(serializers.ModelSerializer):
    author = Profile.objects.all()

    def create(self, validated_data):
        return Publication.objects.create(**validated_data)

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


class ServiceSerializer(serializers.ModelSerializer):
    publication = PublicationSerializer()

    class Meta:
        model = Service
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)

    def create(self, validated_data):
        return Service.objects.create(**validated_data)
