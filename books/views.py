from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from books.forms import BookForm
from .forms import *
from django.urls import reverse_lazy


class BookListView(generic.ListView):
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 2
    queryset = Book.objects.all().order_by('-created_at')


@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.filter(is_active=True).order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            return redirect('book_detail', pk=book.pk)

    else:
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': comments,
        'comment_form': comment_form
    })


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    # form_class = BookForm
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_create.html'


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'
    # form_class = BookForm
    context_object_name = 'book'


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')

# class BookDetailView(generic.DetailView):
#     model = Book
#     # queryset = Book.objects.all()
#     template_name = 'books/book_detail.html'
#
#     def get_context_data(self, **kwargs):
#         # book = self.get_object()
#         kwargs['comments'] = self.get_object().comments.all()
#
#         return super().get_context_data(**kwargs)
