from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView, UserViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list', UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('create', UserCreateView.as_view(), name='user-create')
]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls