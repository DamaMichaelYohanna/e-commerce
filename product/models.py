import os.path

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Store(models.Model):
    """models for a particular seller's store"""
    name = models.CharField(max_length=300)
    full_address = models.TextField()
    lga = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    owner = models.ManyToManyField(User, verbose_name='staffs')
    date_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name}'


def path_to_preview(instance, filename):
    """ get path for saving user head shot """
    return os.path.join('headshot', str(instance.id), filename)


class Preview(models.Model):
    """model for the image thumbnails for product   """
    thumb_1 = models.ImageField()
    thumb_2 = models.ImageField()
    thumb_3 = models.ImageField()
    thumb_4 = models.ImageField()

    def __str__(self):
        return f'{self.thumb_1.url}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return f' -> '.join(full_path[::-1])


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    image = models.ForeignKey("Preview", on_delete=models.SET_NULL, null=True, blank=True)
    percent = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    date_added = models.DateTimeField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.product}'


class OrderItem(models.Model):
    ref_id = models.CharField(max_length=15, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Order)
    date_add = models.DateField(auto_now=True, )

    def get_cart_item(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([items.product.price for items in self.items.all()])

    def __str__(self):
        return f'{self.owner} {self.ref_id}'
