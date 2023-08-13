from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, IndexView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
