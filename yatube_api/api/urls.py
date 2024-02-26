from django.urls import include, path
from rest_framework.routers import SimpleRouter as Router

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = Router()
router_v1.register(
    r'posts',
    PostViewSet,
    basename='posts'
)
router_v1.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post_comments'
)
router_v1.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
