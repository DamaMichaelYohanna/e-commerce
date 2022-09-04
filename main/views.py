from django.shortcuts import render

from product.models import Product


def index(request):
    if 'search' in request.GET:
        search_key = request.GET.get("search")
        print(search_key)
        search_1 = Product.objects.filter(name__icontains=search_key)
        print(search_1)
    men_and_women_fashion = Product.objects.all()
    context = {'fashion': men_and_women_fashion}
    return render(request, 'main/home.html', context)


def quickview(request):
    return render(request, 'main/quickView.html', )


def product_category(request,):
    """View to display the different category of product as requested"""
    category = request.GET.get('category')
    if category == 'fashion':
        detail = Product.objects.all()
        print(detail)
    elif category == 'sport':
        pass
    elif category == 'electronic':
        pass


def view_cart(request):
    context = {}
    return render(request, 'main/cart.html', context=context)


def about_us():
    return None


def contact_us():
    return None


def faq():
    return None