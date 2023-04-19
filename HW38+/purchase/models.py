from django.db import models
from user.models import User
from book.models import Book



class Purchase(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    class Meta:
        db_table = 'purchase'