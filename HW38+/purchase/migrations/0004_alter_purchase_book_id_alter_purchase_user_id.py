# Generated by Django 4.1.7 on 2023-04-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_options'),
        ('user', '0002_alter_user_options'),
        ('purchase', '0003_alter_purchase_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='book_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
