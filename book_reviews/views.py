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

def add_book(request):
    if request.method == 'POST':
        context = {
            'message': 'The book was succesfully added to the library.',
            'show_form': False,
        }
        Book.objects.create(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            description = request.POST.get('description'),
            publish_date = request.POST.get('publish_date'),
            purchase_link = request.POST.get('purchase_link'),
        )
        #try:
            #Book.objects.create(
                #title = request.POST.get('title'),
                #author = request.POST.get('author'),
                #description = request.POST.get('description'),
                #publish_date = request.POST.get('publish_date'),
                #purchase_link = request.POST.get('purchase_link'),
#)
        #except:
            #context['message'] = 'There was an error in adding the book. Please try again.'
            #context['show_form'] = True
        return render(request, 'add_book.html', context)
    else:
        context = {
            'show_form': True,
        }
        return render(request, 'add_book.html', context)



