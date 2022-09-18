from django.urls import path

from vendor import views

urlpatterns = [
    path('', views.dashboard, name='vendor dashboard'),
    path('product/add', views.add_product, name='v_add_product'),
    path('product/update', views.update_product, name='v_update_product'),
    path('product/delete', views.delete_product, name='v_delete_product'),

]