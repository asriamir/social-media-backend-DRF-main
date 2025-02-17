from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
   
    path("add-post/", PostViewSet.as_view({"post": "create"}), name="add_post"),  
    path("posts/", PostViewSet.as_view({"get": "list"}), name="list_posts"),  
    path("post/<int:pk>/", PostViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="post_detail"),
]

urlpatterns += router.urls
