from django.urls import path
from .views import my_view_purchase

urlpatterns = [
    path('', my_view_purchase, name='purchase')
]