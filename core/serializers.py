# encoding: utf-8
from django.contrib.auth.hashers import make_password
from push_notifications.models import GCMDevice
from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'photo')

    def restore_object(self, attrs, instance=None):
        attrs['password'] = make_password(attrs['password'])
        return super(UserSerializer, self).restore_object(attrs, instance=None)


class GCMDeviceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(label=u'Пользователь')

    class Meta:
        model = GCMDevice
        fields = (
            'id',
            'name',
            'active',
            'user',
            'date_created',
            'device_id',
            'registration_id',
        )
        read_only_fields = (
            'active',
        )