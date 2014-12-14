from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import UserList, UserDetail, api_root, CurrentUserView, DeviceDetail, DeviceList
from spotit.views import PostList, PostCommentDetail, PostCommentList, PostDetail, PostUserRatingList, \
    PostUserRatingDetail, PostCommentUserRatingList, PostCommentUserRatingDetail, PostPhotoList, PostPhotoDetail


urlpatterns = patterns('',
    url(r'^$', api_root),
    url(r'^current-user/$', CurrentUserView.as_view(), name='current-user'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^devices/$', DeviceList.as_view(), name='device-list'),
    url(r'^devices/(?P<pk>\d+)/$', DeviceDetail.as_view(), name='device-detail'),
    url(r'^posts/$', PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^posts/comments/$', PostCommentList.as_view(), name='post-comment-list'),
    url(r'^posts/comments/(?P<pk>\d+)/$', PostCommentDetail.as_view(), name='user-comment-detail'),
    url(r'^posts/photos/$', PostPhotoList.as_view(), name='post-photo-list'),
    url(r'^posts/photos/(?P<pk>\d+)/$', PostPhotoDetail.as_view(), name='post-photo-detail'),
    url(r'^posts/ratings/$', PostUserRatingList.as_view(), name='post-rating-list'),
    url(r'^posts/ratings/(?P<pk>\d+)/$', PostUserRatingDetail.as_view(), name='post-rating-detail'),
    url(r'^posts/comments/ratings/$', PostCommentUserRatingList.as_view(), name='post-comment-rating-list'),
    url(r'^posts/comments/ratings/(?P<pk>\d+)/$', PostCommentUserRatingDetail.as_view(), name='user-comment-rating-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)