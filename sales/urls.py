from django.urls import path

from sales import views

namespace = 'sales'
urlpatterns = [
    path('', views.sales, name='home')
]