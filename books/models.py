from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.pk])


class Comment(BaseModel):
    class Meta:
        verbose_name_plural = 'comments'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    recommended = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.content
