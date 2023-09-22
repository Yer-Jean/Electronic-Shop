from django.urls import path

from . import views
from .apps import BlogConfig
from .views import ArticleListView, ArticleCreateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
]
