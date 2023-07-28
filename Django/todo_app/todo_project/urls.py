from django.contrib import admin
from django.urls import path
from todo.views import (add_todo_view, 
                        add_category_view, 
                        display_todos)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add_category/', add_category_view),
    path("add_todo/", add_todo_view),
    path("todos/", display_todos),
]
