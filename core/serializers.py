# encoding: utf-8
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def restore_object(self, attrs, instance=None):
        attrs['password'] = make_password(attrs['password'])
        return super(UserSerializer, self).restore_object(attrs, instance=None)
