from django.shortcuts import render
from django.views import generic
from books.models import Book


class HomePageView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        kwargs['books'] = Book.objects.all().order_by('-created_at')[0:3]
        return super().get_context_data(**kwargs)

    template_name = 'home.html'
