from django.urls import path

from product import views

app_name = 'product'
urlpatterns = [
    path('', views.product, name='home'),
    path('category/<str:category_keyword>', views.product_category, name='category'),
    path('quickview/<int:pk>', views.quickview, name="quick_view"),
    # cart related urls
    path('cart', views.view_cart, name='cart'),
    path('cart/<int:pk>/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:pk>/remove', views.remove_from_cart, name='remove_for_cart'),
    path('cart/clear', views.cancel_selection, name='cancel_selection'),
    path('checkout', views.check_out, name='check'),
]