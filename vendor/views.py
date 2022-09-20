from django.shortcuts import render, redirect

from product.models import Category
from vendor.forms import ProductForm, ProductImage


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        product_image = ProductImage(request.FILES)
        category = Category.objects.get(name=request.POST.get("category"))
        if product_form.is_valid:
            if product_image.is_valid():
                image_obj = product_image.save()

            product_obj = product_form.save(commit=False)
            product_obj.image = image_obj
            product_obj.category = category

        return redirect('vendor:dashboard')
    else:
        product_form = ProductForm()
        product_image = ProductImage()
        context = {'product_form': product_form, 'product_image': product_image}
        return render(request, 'vendor/add_product.html', context)


def update_product(request):
    pass


def delete_product(request):
    pass


def dashboard(request):
    pass
