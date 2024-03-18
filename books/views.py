from django.shortcuts import render
from django.views import generic
from books.forms import BookForm
from .forms import *
from django.urls import reverse_lazy


class BookListView(generic.ListView):
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 2
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    # form_class = BookForm
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'
    # form_class = BookForm
    context_object_name = 'book'


class BookDeleteView(generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')
