from django.urls import path

from vendor import views

app_name = 'vendor'
urlpatterns = [
    path('', views.dashboard, name='vendor dashboard'),
    path('product/add', views.add_product, name='v_add_product'),
    path('product/<int:pk>/update', views.update_product, name='v_update_product'),
    path('product/<int:pk>/delete', views.delete_product, name='v_delete_product'),

]