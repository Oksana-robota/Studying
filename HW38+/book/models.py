from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    author = models.CharField(max_length=255, null=False, unique=True)
    year = models.DateField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
