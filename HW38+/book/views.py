from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    # success_url = reverse_lazy()


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
