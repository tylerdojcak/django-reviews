from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
        'title': 'Cohort 13A Reviews'
    }
    return render(request, 'index.html', context)

def books(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
        'title': 'Library'
    }
    return render(request, 'books.html', context)
