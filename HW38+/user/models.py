from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'User with id - {self.id}: {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return f'detail/{self.id}'
