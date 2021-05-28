"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from book_reviews import views as book_review_views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', book_review_views.index, name='index'),
    path('accounts/', account_views.register, name='register'),
    path('books/', include('book_reviews.urls'), name='books'),
    path('books/add', book_review_views.add_book, name='add_book'),
    path('login/', auth_views.LoginView.as_view(extra_context={'title': 'test extra_content'}), name='login'), # override
    path('', include('django.contrib.auth.urls'), name='login'),
    path('admin/', admin.site.urls),
]
