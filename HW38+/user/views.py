from django.http import HttpResponse
from .models import User
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserForm


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm

# simple views
# def my_view(request):
#     user = User.objects.all()
#     user_all = [{
#         'id': i.id,
#         'first_name': i.first_name,
#         'last_name': i.last_name,
#         'age': i.age
#     } for i in user]
#     return HttpResponse(user_all)
