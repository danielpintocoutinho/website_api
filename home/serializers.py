from rest_framework import serializers

from home.models import Category

class HomeSerializer(serializers.Serializer):
    summary = serializers.CharField()
    covers = serializers.ListField()


class AboutSerializer(serializers.Serializer):
    about = serializers.CharField()
    image = serializers.ImageField()


class SectionsSerializer(serializers.Serializer):
    sections = serializers.ListField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["label"]