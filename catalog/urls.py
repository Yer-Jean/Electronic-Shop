from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import CategoryListView, ProductListView, ProductDetailView, IndexView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('products/<int:pk>/', ProductListView.as_view(), name='category'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('categories/', CategoryListView.as_view(), name='categories'),

    path('contacts/', views.contacts, name='contacts'),
]
