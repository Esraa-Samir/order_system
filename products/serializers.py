from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'price',
            'price_currency',
            'is_available'
        )


