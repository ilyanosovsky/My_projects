from django.contrib import admin
from django.urls import path, include
from posts.views import PostListView, PostDetailView, UserDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/posts/", PostListView.as_view(), name="posts"),
    path("api/posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("api/posts/<int:pk>/", PostView.as_view(), name="post-detail"),
    path("api/user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
