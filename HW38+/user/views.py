# from django.http import HttpResponse
from .models import User
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import UserForm
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
# from rest_framework.generics import ListAPIView
import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


# class UserListView(ListView):
#     model = User
#
#
# class UserDetailView(DetailView):

#     model = User
#     template_name = 'user_detail.html'
#
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm


# DRF
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['contains'],
            'age': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'

# HW 41
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['age']
    pagination_class = CustomPaginator
    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

# generic views
# class UserListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


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
