# Generated by Django 3.2 on 2021-06-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0003_book_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reviews',
            field=models.JSONField(),
        ),
    ]
