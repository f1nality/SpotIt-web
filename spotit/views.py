from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from core.models import User
from serializers import UserSerializer, PostSerializer, PostCommentSerializer
from spotit.models import Post, PostComment


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'posts': reverse('post-list', request=request),
        'posts-comments': reverse('post-comment-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer


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
