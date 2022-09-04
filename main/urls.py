from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about_us, name='about'),
    path('contact', views.contact_us, name='contact'),
    path('faq', views.faq, name='faq'),
]