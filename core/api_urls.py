from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import UserList, UserDetail, api_root
from spotit.views import PostList, PostCommentDetail, PostCommentList, PostDetail


urlpatterns = patterns('',
    url(r'^$', api_root),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^posts/$', PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^posts/comments/$', PostCommentList.as_view(), name='post-comment-list'),
    url(r'^posts/comments/(?P<pk>\d+)/$', PostCommentDetail.as_view(), name='user-comment-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)