from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list'),
    path('create_poduct_post/', views.create, name='create'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('delete_product_post/<int:product_id>', views.delete_product_post, name='delete_product_post'),
]