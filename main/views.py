from django.shortcuts import render

from product.models import Product, Category


def index(request):
    search_key = request.GET.get("keyword")
    category_keyword = request.GET.get("category")
    print(search_key, category_keyword)
    if search_key and category_keyword:  # if both search key and category are available
        category = Category.objects.get(name=category_keyword)
        search_product = Product.objects.filter(category=category, name__icontains=search_key)
    elif search_key:  # only search key without category
        search_product = Product.objects.filter(name__icontains=search_key)
    else:
        search_product = None

    # render(request, 'main/search.html', {'product': product})
    all_products = Product.objects.all()  # grab all product
    all_category = Category.objects.all()  # grab all the categories
    # filter sub categories from all category.
    fashion_category = all_category.get(name='Fashion')  # grab fashion sub cat
    electronic_category = all_category.get(name='Electronics')  # grab fashion sub cat
    sport_category = all_category.get(name='Sport')  # grab fashion sub cat
    # filter products now base on categories
    # for item in fashion_category:
    #     sub_cat = fashion_category.
    # fashion = [fashion_category]
    # # parent_cat = fashion[0].parent
    # while fashion_category is not None:
    #     fashion.append(fashion_category.name)
    #     print(fashion_category.name)
    #     # k = k.parent
    print(fashion_category.children.all())
    fashion = all_products.filter(category__in=fashion_category.children.all())
    electronics = all_products.filter(category__in=electronic_category.children.all())
    sport_and_out_door = all_products.filter(category__in=sport_category.children.all())
    context = {'fashion': fashion, 'sport': sport_and_out_door,
               'electronic': electronics, 'search_result': search_product}
    return render(request, 'main/home.html', context)


def search(request):
    """Search functionality"""
    search_key = request.GET.get("search")
    category_keyword = request.GET.get("category")
    if search_key and category_keyword:  # if both search key and category are available
        category = Category.objects.get(name=category_keyword)
        product = Product.objects.filter(category=category, name__icontains=search_key)
    elif search_key:  # only search key without category
        product = Product.objects.filter(name__icontains=search_key)

    render(request, 'main/search.html', {'product': product})


def quickview(request):
    return render(request, 'main/quickView.html', )


def about_us(request):
    return render(request, 'main/about.html')


def contact_us(request):
    return render(request, 'main/contact.html')


def faq(request):
    return render(request, 'main/faq.html')