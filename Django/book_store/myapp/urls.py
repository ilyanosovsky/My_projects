from django.urls import path
from .views import BookList, BookDetail,book_all,book_create,book_update,book_delete,shop

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/all/', book_all, name='book-all'),
    path('books/create/', book_create, name='book-create'),
    path('books/update/<int:pk>/', book_update, name='book-update'),
    path('books/delete/<int:pk>/', book_delete, name='book-delete'),
    path('shop', shop, name='shop'),
]