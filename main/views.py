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


def search(request):
    search_key = request.GET.get("search")
    category = request.GET.get("category")
    if search_key and category:  # if both search key and category are available
        pass
    elif search_key:  # only search key without category
        pass
    else:
        pass


def quickview(request):
    return render(request, 'main/quickView.html', )


def about_us(request):
    return render(request, 'main/about.html')


def contact_us(request):
    return render(request, 'main/contact.html')


def faq(request):
    return render(request, 'main/faq.html')