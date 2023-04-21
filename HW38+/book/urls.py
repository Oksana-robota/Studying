from django.urls import path
from .views import my_view_book

urlpatterns = [
    path('', my_view_book, name='book')
]