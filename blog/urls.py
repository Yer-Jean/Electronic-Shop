from django.urls import path

from . import views
from .apps import BlogConfig
from .views import ArticleListView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<str:slug>/', ArticleDetailView.as_view(), name='article'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),

]
