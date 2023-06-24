from django.contrib import admin
from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('hello/', views.index),
    path('products/', views.products, name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/add', views.ProductCreateView.as_view(), name='product_add'),
    path('products/update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/mine', views.product_mine, name='product_mine'),
]
