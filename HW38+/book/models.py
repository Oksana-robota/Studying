from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    author = models.CharField(max_length=255, null=False, unique=True)
    year = models.DateField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'''The book {self.title} with id - {self.id} was written by {self.author} in {self.year}.
                    It's price is {self.price}'''
