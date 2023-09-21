from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import CategoryListView, ProductListView, ProductDetailView, IndexView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('contacts/', views.contacts),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='category'),
]
