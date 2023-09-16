from django.urls import path

from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.index),
    path('<int:pk>/product/', views.product, name='product'),
    path('contacts/', views.contacts),
]
