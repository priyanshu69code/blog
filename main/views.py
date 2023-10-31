from django.shortcuts import render, get_object_or_404
from .logics import get_top_10_recent_articles, get_article
from main import models
# Create your views here.


def index(request):
    top_10_recent_articles = get_top_10_recent_articles()
    return render(request, 'main/index.html', {'top_10_recent_articles': top_10_recent_articles})


def article(request, pk):
    article = get_object_or_404(models.Articles, pk=pk)
    context = {
        "article": article
    }

    return render(request, "main/article.html", context)


def author(request, pk):
    author = get_object_or_404(models.Author, pk=pk)
    context = {
        "author": author
    }

    return render(request, "main/author.html", context)
