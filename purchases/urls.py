from django.urls import path
from purchases.views import *

app_name = 'purchases'

urlpatterns = [
    path('', PurchaseProductView.as_view({'post': 'create'}), name='create-purchase'),
    path('history',PurchaseListView.as_view({'get': 'list'}),name='list-purchases'),
    path('Revenue',PurchaseRevenueView.as_view({'get': 'list'}),name='get-Revenue'),
    # path('delete/<int:pk>',ProductDeleteView.as_view({'delete': 'destroy'}),name='delete-product')
]