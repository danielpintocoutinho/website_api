from rest_framework import serializers
from projects.models import Project


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'cover', 'title']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'cover', 'title', 'description']