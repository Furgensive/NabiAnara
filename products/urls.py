from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.index, name='products_list'),
    path('new/', views.new, name='new_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]