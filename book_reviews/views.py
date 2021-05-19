from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'template.html')

def books(request):
    return render(request, 'books.html')
