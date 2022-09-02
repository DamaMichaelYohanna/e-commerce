from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name="logout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create/user', views.customer_register, name='user_register'),
]