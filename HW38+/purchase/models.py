from django.db import models
from user.models import User
from book.models import Book
from django.urls import reverse

class Purchase(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=False)

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f'User ({self.user_id}) bought book - {self.book_id} on {self.date}'

    def get_absolute_url(self):
            return f'detail/{self.id}'