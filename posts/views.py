from rest_framework import generics

from posts.models import Post
from posts.serializers import PostSerializer, PostShortSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostShortSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer