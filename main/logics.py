from .models import Articles
from main import models


def get_top_10_recent_articles():
    # Query the Articles model and order the results by the 'createdAt' field in descending order.
    # Then, slice the result to get the top 10 most recent articles.
    top_10_recent_articles = Articles.objects.all().order_by('-createdAt')[:10]
    return top_10_recent_articles


def get_article(pk):
    return Articles.objects.get(pk=pk)
