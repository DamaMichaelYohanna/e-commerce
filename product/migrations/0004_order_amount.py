# Generated by Django 4.0.4 on 2022-08-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
