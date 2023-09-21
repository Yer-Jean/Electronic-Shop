from django.urls import path

from . import views
from .apps import BlogConfig
from .views import ArticleListView


app_name = BlogConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles')
]
