import datetime as dt
from . import models
from .models import OrderItem


def cart_context_processor(request):
    """context processor to display all the items in the cart"""
    try:
        order_object = OrderItem.objects.get(owner=request.user)
        order_item = order_object.items.all()
        total_item = order_object.items.all().count()
        total_item_price = sum([item.product.price for item in order_object.items.all()])

    except TypeError:
        order_item = None
        total_item = 0
        total_item_price = 0

    except OrderItem.DoesNotExist:
        order_item = None
        total_item = 0
        total_item_price = 0

    return {'cart': order_item, 'cart_item': total_item, 'items_total_price': total_item_price}
