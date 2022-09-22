from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from product.models import Category, Product, Preview
from vendor.forms import ProductForm, ProductImage


@login_required
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


@login_required
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        category = Category.objects.get(name=product.category.name)
        images = Preview.objects.get(pk=product.image.pk)
    except Product.DoesNotExit:
        pass
    except Category.DoesNotExist:
        pass
    except Preview.DoesNotExist:
        pass

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
        product_form = ProductForm(instance=product)
        product_image = ProductImage(instance=images)
        context = {'product_form': product_form, 'product_image': product_image}
        return render(request, 'vendor/add_product.html', context)


@login_required
def delete_product(request):
    pass


@login_required
def dashboard(request):
    pass
