from django.db import models
from djmoney.models.fields import MoneyField
from users.models import User
from products.models import Product
from django.db.models import Sum
from django.conf import settings
from users.models import User


class Purchase(models.Model):
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default="")
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default="")
    date = models.DateTimeField(auto_now_add=True)
    # price = MoneyField(decimal_places=4, max_digits=19, default_currency='EGP', default=0)

    @property
    def get_item(self, obj):
        return Product.objects.get(id= obj.item)



