from django.http import  HttpResponse
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from .forms import PurchaseForm


class PurchaseListView(ListView):
    model = Purchase

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm









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
