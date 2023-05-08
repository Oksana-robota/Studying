from django.http import HttpResponse
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from .forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer
import django_filters
from rest_framework import filters


# class PurchaseListView(ListView):
#     model = Purchase
#
#
# class PurchaseDetailView(DetailView):
#     model = Purchase
#     template_name = 'purchase_detail.html'
#
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     form_class = PurchaseForm

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'date': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ['user_id', 'book_id']
    ordering_fields = ['date']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
# simple views
# def my_view_purchase(request):
#     purchases = Purchase.objects.all()
#     purchase_all = [{
#         'id': i.id,
#         'user_id': i.user_id,
#         'book_id': i.book_id,
#         'date': i.date,
#     } for i in purchases]
#     return HttpResponse(purchase_all)
