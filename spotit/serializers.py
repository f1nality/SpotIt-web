# encoding: utf-8
from rest_framework import serializers
from core.models import User
from spotit.models import Post, PostComment, PostUserRating, PostCommentUserRating


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(label=u'Автор')

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
    post = serializers.PrimaryKeyRelatedField(label=u'Пост')
    author = serializers.PrimaryKeyRelatedField(label=u'Автор')

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


class PostPhotoSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(label=u'Пост')

    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'image',
            'date_add',

        )
        read_only_fields = (
            'post',
            'image',
            'date_add',
        )


class PostUserRatingSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(label=u'Пост')

    class Meta:
        model = PostUserRating
        fields = (
            'id',
            'post',
            'user',
            'vote',
            'date',

        )


class PostCommentUserRatingSerializer(serializers.HyperlinkedModelSerializer):
    post_comment = serializers.PrimaryKeyRelatedField(label=u'Комментарий')

    class Meta:
        model = PostCommentUserRating
        fields = (
            'id',
            'post_comment',
            'user',
            'vote',
            'date',

        )