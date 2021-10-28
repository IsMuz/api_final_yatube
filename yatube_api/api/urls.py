from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupGetList, GroupGetDetail, \
    CommentViewSet, FollowGetPost

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/groups/', GroupGetList.as_view()),
    path('v1/groups/<group_id>/', GroupGetDetail.as_view()),
    path('v1/follow/', FollowGetPost.as_view()),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
