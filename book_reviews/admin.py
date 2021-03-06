from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'purchase_link', 'reviews')

admin.site.register(Book, BookAdmin)
