from django.contrib import admin
from books.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'content', 'book', 'is_active', 'recommended' ,'created_at',
    ]
