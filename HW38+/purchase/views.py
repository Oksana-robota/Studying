from django.http import HttpResponse
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from .forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

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
