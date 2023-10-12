from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import CategoryListView, ProductListView, ProductDetailView, IndexView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, VersionUpdateView, VersionListView, VersionDeleteView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category'),

    path('categories/', CategoryListView.as_view(), name='categories'),

    path('product/<int:pk>/versions/', VersionListView.as_view(), name='version_list'),
    path('product/version/create/', VersionCreateView.as_view(), name='version_create'),
    path('product/version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('product/version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),

    path('contacts/', views.contacts, name='contacts'),
]
