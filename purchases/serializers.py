from rest_framework import serializers
from .models import Purchase
from products.serializers import ProductSerializer
from products.models import Product

class PurchaseSerializer(serializers.ModelSerializer):
    purchaser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # item = serializers.Field()

    class Meta:
        model = Purchase
        fields = (
            'item',
            'purchaser',
            'date',
        )


class PurchaseProductSerializer(serializers.ModelSerializer):
    purchaser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    item = ProductSerializer()

    class Meta:
        model = Purchase
        fields = (
            'item',
            'purchaser',
            'date',
        )