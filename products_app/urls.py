from django.urls import path
from .views import create_product, get_products, update_product, partial_update_product, delete_product

urlpatterns = [
    path('products/', get_products, name='product-list'),
    path('products/<int:pk>/', get_products, name='product-detail'),
    path('products/create/', create_product, name='product-create'),
    path('products/update/<int:pk>/', update_product, name='product-update'),
    path('products/partial-update/<int:pk>/', partial_update_product, name='product-partial-update'),
    path('products/delete/<int:pk>/', delete_product, name='product-delete'),
]
