# Generated by Django 3.2 on 2021-04-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0005_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='price_currency',
        ),
    ]