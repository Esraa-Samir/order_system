from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle


class ProductCreateListView(viewsets.ModelViewSet):
    """
    View all products / add a new product (by an admin).
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_fields = ('name', )
    permission_classes = [IsAdmin, IsAuthenticated]
    throttle_classes = [UserRateThrottle]


class ProductUpdateView(viewsets.ModelViewSet):
    """
    View to update a product (by an admin).
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdmin, IsAuthenticated]
    throttle_classes = [UserRateThrottle]


class ProductDeleteView(viewsets.ModelViewSet):
    """
    View to delete a product (by an admin).
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdmin, IsAuthenticated]
    throttle_classes = [UserRateThrottle]


class AvailableProductListView(viewsets.ModelViewSet):
    """
    View all available products (by normal users).
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    filter_fields = ('name', )
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
