from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
