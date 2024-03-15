from django.contrib import admin
from books.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...
