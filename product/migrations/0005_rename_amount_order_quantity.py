# Generated by Django 4.0.4 on 2022-08-26 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='quantity',
        ),
    ]
