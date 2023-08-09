from django.urls import path

from catalog.views import index, contacts, ProductDetailView

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail')
]