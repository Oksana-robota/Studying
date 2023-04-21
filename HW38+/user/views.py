from django.http import  HttpResponse
from .models import User


def my_view(request):
    user = User.objects.all()
    user_all = [{
        'id': i.id,
        'first_name': i.first_name,
        'last_name': i.last_name,
        'age': i.age
    } for i in user]
    return HttpResponse(user_all)