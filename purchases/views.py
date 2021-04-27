from django.shortcuts import render
from rest_framework import viewsets
from .models import Purchase
from products.models import Product
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from django.db.models import Sum


class PurchaseProductView(viewsets.ModelViewSet):
    """
    Purchase a product.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    permission_classes = [IsNotOwner, IsAuthenticated, IsAvailable]
    throttle_classes = [UserRateThrottle]


class PurchaseListView(viewsets.ModelViewSet):
    """
    View all user's purchases.
    """
    serializer_class = PurchaseProductSerializer
    permission_classes = [IsNotAdmin, IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        id = self.request.user.id
        if id is not None:
            queryset = Purchase.objects.filter(purchaser__id=id)
        return queryset


class PurchaseRevenueView(viewsets.ModelViewSet):
    """
    View total Revenue.
    """
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdmin, IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def list(self, request):
        profit = Purchase.objects.all().aggregate(Sum('item__price'))['item__price__sum']
        return Response({'Revenue': Revenue})
