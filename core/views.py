from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import User, Device
from core.serializers import UserSerializer, DeviceSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'current-user': reverse('current-user', request=request),
        'users': reverse('user-list', request=request),
        'devices': reverse('device-list', request=request),
        'posts': reverse('post-list', request=request),
        'posts-photos': reverse('post-photo-list', request=request),
        'posts-comments': reverse('post-comment-list', request=request),
        'posts-ratings': reverse('post-rating-list', request=request),
        'posts-comments-ratings': reverse('post-comment-rating-list', request=request),
    })


class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    filter_fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')
    ordering_fields = '__all__'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    filter_fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')


class DeviceList(generics.ListCreateAPIView):
    model = Device
    serializer_class = DeviceSerializer
    filter_fields = ('id', 'user', 'name', 'unique_id', 'date_add',)
    ordering_fields = '__all__'


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Device
    serializer_class = DeviceSerializer
    filter_fields = ('id', 'user', 'name', 'unique_id', 'date_add',)
