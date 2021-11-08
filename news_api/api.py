from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from .views import PostViewSet, CommentViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

posts_router = router.register("posts", PostViewSet)
posts_router.register(
    "comments", CommentViewSet, basename="post-comments", parents_query_lookups=["post"]
)
