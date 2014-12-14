# encoding: utf-8
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from core.models import User, Device


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')

    def restore_object(self, attrs, instance=None):
        attrs['password'] = make_password(attrs['password'])
        return super(UserSerializer, self).restore_object(attrs, instance=None)


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(label=u'Пользователь')

    class Meta:
        model = Device
        fields = (
            'id',
            'user',
            'name',
            'unique_id',
            'date_add',
        )
        read_only_fields = (
            'date_add',
        )