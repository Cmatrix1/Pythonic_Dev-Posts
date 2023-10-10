from django.db import models
from datetime import timezone


# Property Pattern
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()

    @property
    def is_published(self):
        return self.published_date < timezone.now().date()


book = Book.objects.get(pk=1)
print(book.is_published)


# Custom Model Managers Pattern
class BookManager(models.Manager):
    def by_author(self, author):
        return self.filter(author=author)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()

    objects = BookManager()

books = Book.objects.by_author('Jane Austen')
