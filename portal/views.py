from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView

from .models import Book
from .models import Author

class IndexView(TemplateView):
    template_name = "index.html"

class AuthorsListView(ListView):
    model = Author

class BooksListView(ListView):
    model = Book

class AuthorDetailView(DetailView):
    model = Author

class BookDetailView(DetailView):
    model = Book