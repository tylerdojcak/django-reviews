# Generated by Django 3.2 on 2021-05-26 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
