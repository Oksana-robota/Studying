# Generated by Django 4.1.7 on 2023-04-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
