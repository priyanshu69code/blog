from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("articles/<int:pk>", views.article, name="get_article"),
    path("author/<int:pk>", views.author, name="get_author"),
    path("articles", views.create_articles, name="create_articles")
]
