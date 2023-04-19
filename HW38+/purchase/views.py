from django.http import  HttpResponse
from .models import Purchase


def my_view_purchase(request):
    purchases = Purchase.objects.all().order_by('date')
    purchase_all = [{
        'id': i.id,
        'user_id': i.user_id,
        'book_id': i.book_id,
        'date': i.date,
    } for i in purchases]
    return HttpResponse(purchase_all)
