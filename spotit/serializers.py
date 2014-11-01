from rest_framework import serializers
from core.models import User
from spotit.models import Post, PostComment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'text',
            'date_add',
            'author_ip',
            'rating',
            'count_vote',
            'count_comments',
            'latitude',
            'longitude'
        )
        read_only_fields = (
            'date_add',
            'rating',
            'count_vote',
            'count_comments'
        )


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField()
    author = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = PostComment
        fields = (
            'post',
            'author',
            'text',
            'date_add',
            'author_ip',
            'rating',
            'count_vote',
            'deleted',
            'latitude',
            'longitude'
        )
        read_only_fields = (
            'date_add',
            'rating',
            'count_vote',
            'deleted'
        )