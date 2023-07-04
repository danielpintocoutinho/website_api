from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    related_posts = serializers.SerializerMethodField()

    def get_related_posts(self, obj):
        posts = []
        for category in obj.category.all():
            posts.extend(Post.objects.filter(category=category).exclude(path=obj.path))
        related = PostShortSerializer(posts, source='posts', many=True, read_only=True).data
        return related

    class Meta:
        model = Post
        fields = ["path", "title", "content", "date", "category", "related_posts"]

class PostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["path", "title"]