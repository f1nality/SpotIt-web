from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from core.models import User
from core.serializers import UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'posts': reverse('post-list', request=request),
        'posts-photos': reverse('post-photo-list', request=request),
        'posts-comments': reverse('post-comment-list', request=request),
        'posts-ratings': reverse('post-rating-list', request=request),
        'posts-comments-ratings': reverse('post-comment-rating-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    filter_fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')
    ordering_fields = '__all__'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    filter_fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')