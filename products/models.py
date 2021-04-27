from django.db import models
from djmoney.models.fields import MoneyField
import requests
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Product name")
    description = models.TextField(help_text="Product description")
    price = MoneyField(decimal_places=4, max_digits=19, help_text="Product price", default_currency='EGP')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default='')
    is_available = models.BooleanField(default=True)

    @property
    def get_price(self, obj):
        access_key = 'dd7cab1936df6770dcab003182652045'
        from_curr = obj.price_currency
        to_curr = User.objects.filter(email=self.context['request'].user).values('currency')[0]['currency']
        amount = obj.price.amount
        """"
        convert currency api endpoint is not available for basic plan in fixer.io
        """
        url = f'http://data.fixer.io/api/latest?access_key={access_key}'
        response = json.loads(requests.get(url).text)
        rates = response['rates']
        temp = float(amount) / rates[from_curr]
        price_converted = temp * rates[to_curr]
        return price_converted

    @property
    def get_price_currency(self, obj):
        to_curr = User.objects.filter(email=self.context['request'].user).values('currency')[0]['currency']
        return to_curr

