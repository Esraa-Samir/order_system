# Generated by Django 3.2 on 2021-04-23 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_quantity'),
        ('purchases', '0007_auto_20210423_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
    ]
