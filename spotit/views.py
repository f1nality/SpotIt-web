from rest_framework import generics
from serializers import PostSerializer, PostCommentSerializer
from spotit.models import Post, PostComment


class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer


class PostCommentList(generics.ListCreateAPIView):
    model = PostComment
    serializer_class = PostCommentSerializer


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PostComment
    serializer_class = PostCommentSerializer
