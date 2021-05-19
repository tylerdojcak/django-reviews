from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'template.html', context)

def books(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'books.html', context)
