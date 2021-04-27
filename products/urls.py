from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('',ProductCreateListView.as_view({'get': 'list', 'post': 'create'}),name='create/list-products'),
    path('update/<int:pk>',ProductUpdateView.as_view({'patch': 'update'}),name='update-product'),
    path('delete/<int:pk>',ProductDeleteView.as_view({'delete': 'destroy'}),name='delete-product'),
    path('available',AvailableProductListView.as_view({'get': 'list'}), name='list-available-products')
]