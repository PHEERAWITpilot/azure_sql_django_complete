from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:store_id>/', views.StoreDetailUpdateDelete.as_view(), name='store_detail'),
    path('stores/deleteAll/', views.StoreDeleteAll.as_view(), name='store_delete_all'),
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetailUpdateDelete.as_view(), name='product_detail'),
    path('products/deleteAll/', views.ProductDeleteAll.as_view(), name='product_delete_all'),
]
