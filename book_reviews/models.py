from django.db import models
import datetime

# Create your models here.

def my_default():
    return {}

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    publish_date = models.DateField(default=datetime.date.today)
    purchase_link = models.CharField(max_length=450, default='http://www.amazon.com')
    reviews = models.JSONField(default=my_default)