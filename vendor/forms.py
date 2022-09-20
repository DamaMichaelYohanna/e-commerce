from django.forms import ModelForm

from product.models import Product, Preview


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImage(ModelForm):
    class Meta:
        model = Preview
        exclude = ('category', )
    pass