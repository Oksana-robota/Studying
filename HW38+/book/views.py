from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from .forms import BookForm
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    # success_url = reverse_lazy()

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
