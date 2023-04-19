from django.http import  HttpResponse
from .models import Book


def my_view_book(request):
    books = Book.objects.all()
    book_all = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
    } for book in books]
    return HttpResponse(book_all)
