from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
import django_filters
from rest_framework import filters


# class BookListView(ListView):
#     model = Book
#
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'
#
#
# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookForm


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'price': ['gte', 'lte', 'gt', 'lt', 'exact']
        }

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['year']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]


# simple views
# def my_view_book(request):
#     books = Book.objects.all()
#     book_all = [{
#         'id': book.id,
#         'title': book.title,
#         'author': book.author,
#         'year': book.year,
#         'price': book.price
#     } for book in books]
#     return HttpResponse(book_all)
