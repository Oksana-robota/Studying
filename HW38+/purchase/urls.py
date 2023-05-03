from django.urls import path
from .views import PurchaseDetailView, PurchaseListView, PurchaseCreateView, PurchaseViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    # path('', my_view_purchase, name='purchase'),
    path('list', PurchaseListView.as_view(), name='purchase_list'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create')
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
