from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isbn = models.CharField(max_length=13, unique=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=total_copies)

    def __str__(self):
        return self.title