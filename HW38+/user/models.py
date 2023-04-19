from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'