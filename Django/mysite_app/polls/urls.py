from django.urls import path
from .views import (posts,
                    profile,
                    add_category_view,
                    add_post_view,
                    AddCategoryView, 
                    AddPostView,
                    PostList,
                    manage_categories,
                    manage_posts)
urlpatterns = [
    # path('posts/', posts, name='posts'),
    path('posts/', PostList.as_view(), name='posts'),
    path('profile/', profile),
    # path('add-category/', add_category_view, name='add-category'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    # path('add-post/', add_post_view, name='add-post'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('manage-categories/', manage_categories, name='manage-categories'),
    path('manage-posts/', manage_posts, name='manage-posts'),

]
