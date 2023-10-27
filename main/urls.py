from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("articles/<int:pk>", views.article, name="get_article")
]
