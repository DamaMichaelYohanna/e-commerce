import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product, Order, OrderItem, Category


def product():
    return None


def product_category(request, category_keyword):
    """View to display the different category of product as requested"""
    # category_keyword = request.GET.get('category')
    category = Category.objects.get(name=category_keyword).children.all()
    print(category)
    products = Product.objects.filter(category__in=category)
    print(products)
    context = {'products': products, 'category': category}
    return render(request, 'product/category.html', context)


def quickview(request, pk):
    product_obj = Product.objects.get(pk=pk)
    context = {'product': product_obj}
    return render(request, 'main/quickView.html', context)


# ----------------------------------------------
# cart section
@login_required()
def add_to_cart(request, pk):
    """view to add item to cart"""
    user = request.user
    item = Product.objects.get(pk=pk)
    order = Order.objects.create(product=item, owner=user)
    order_item, status = OrderItem.objects.get_or_create(owner=user, )
    order_item.items.add(order)
    order.ref_id = random.randint(0, 100)
    order.save()
    messages.success(request, "Item has been added to cart successfully")
    return redirect('/')


@login_required()
def remove_from_cart(request, pk,):
    """view to remove an item from the cart"""
    user = request.user.id
    product = get_object_or_404(Product, pk=pk)
    item = Order.objects.filter(product__name=product, owner=user, )[0]
    order_item = OrderItem.objects.get(owner=user)
    order_item.items.remove(item)
    order_item.save()
    item.delete()
    if 'state' in request.GET:
        return redirect('/products/cart')
    return redirect('/')


@login_required
def view_cart(request):
    if request.method == 'POST':
        owner = request.user
        goods = request.POST.get("goods")
        amount = request.POST.get("amount")
        print(goods, amount)
        item = Order.objects.get(owner=owner, product__name=goods)
        item.quantity = amount
        item.save()
        messages.success(request, "Quantity updated successfully")
        # if the quantity has been updated
    try:  # try to get cart item for a user if authenticated
        cart_item_obj = OrderItem.objects.get(owner=request.user)
        cart_item_list = cart_item_obj.items.all()
        cart_item_price = sum([item.product.price * item.quantity for item in cart_item_obj.items.all()])
    except TypeError:  # if error occur from user not logged in
        cart_item_list = None
        cart_item_price = 0

    except OrderItem.DoesNotExist:  # if cart is empty
        cart_item_list = None
        cart_item_price = 0

    context = {'cart_item': cart_item_list, 'cart_item_price': cart_item_price}
    return render(request, 'product/cart.html', context=context)


@login_required()
def cancel_selection(request):
    user = request.user.id
    order = Order.objects.filter(owner=user)
    order.delete()
    order_item = OrderItem.objects.get(owner=user)
    order_item.delete()
    del order
    return redirect('/')


@login_required()
def check_out(request):
    user = request.user.pk
    try:
        order_list = OrderItem.objects.get(owner=user).items.all()
    except:
        order_list = None
        price = None
        quantity = None
    else:
        price = f'{sum([item.product.price for item in order_list]):,}'
        quantity = order_list.count()

    context = {'items': order_list,
               'section': 'Check out',
               'sub_total': price, 'q': quantity}
    return render(request, 'product/checkout.html', context)

# def generate_reference(request):
#     user = request.user.pk
#     code = generate_ref_code()
#     order_list = OrderItem.objects.get(owner=user)
#     all_order_list = [order.ref_id for order in OrderItem.objects.all()]
#     if code in all_order_list:
#         code = generate_ref_code()
#     else:
#         pass
#
#     print(all_order_list)
#     try:
#         order_list.ref_id = code
#     except:
#         order_list.ref_id = generate_ref_code()
#
#     order_list.save()
#     print(code)
#     context = {'code': code, 'section': 'Reference code'}
#     return render(request, 'reference.html', context)
