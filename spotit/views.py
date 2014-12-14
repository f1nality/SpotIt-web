from rest_framework import generics
from serializers import PostSerializer, PostCommentSerializer, PostUserRatingSerializer, PostCommentUserRatingSerializer
from spotit.models import Post, PostComment, PostCommentUserRating, PostUserRating


class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer
    filter_fields = (
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
    ordering_fields = '__all__'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    filter_fields = (
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


class PostCommentList(generics.ListCreateAPIView):
    model = PostComment
    serializer_class = PostCommentSerializer
    filter_fields = (
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
    ordering_fields = '__all__'


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PostComment
    serializer_class = PostCommentSerializer
    filter_fields = (
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


class PostUserRatingList(generics.ListCreateAPIView):
    model = PostUserRating
    serializer_class = PostUserRatingSerializer
    filter_fields = (
        'id',
        'post',
        'user',
        'vote',
        'date',
    )
    ordering_fields = '__all__'


class PostUserRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PostUserRating
    serializer_class = PostUserRatingSerializer
    filter_fields = (
        'id',
        'post',
        'user',
        'vote',
        'date',
    )


class PostCommentUserRatingList(generics.ListCreateAPIView):
    model = PostCommentUserRating
    serializer_class = PostCommentUserRatingSerializer
    filter_fields = (
        'id',
        'post_comment',
        'user',
        'vote',
        'date',
    )
    ordering_fields = '__all__'


class PostCommentUserRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PostCommentUserRating
    serializer_class = PostCommentUserRatingSerializer
    filter_fields = (
        'id',
        'post_comment',
        'user',
        'vote',
        'date',
    )