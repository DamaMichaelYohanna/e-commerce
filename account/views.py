from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from account.models import User


def login_view(request):
    """login view"""
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user=user)
            messages.success(request, 'Login successful')
            return redirect(reverse_lazy("account:dashboard"))
        else:
            return render(request, 'account/login.html', {'err': True})

    else:
        return render(request, 'account/login.html')


def logout_view(request):
    """log out view"""
    logout(request)
    redirect(reverse_lazy("main:home"))


def customer_register(request):
    """View for registering customer into our side."""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            print(email, password)
            try:
                user = User.objects.create(email=email)
            except IntegrityError:
                return render(request, 'account/register.html', {'err': True})
            else:
                user.set_password(password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect(reverse_lazy('main:home'))
        else:  # if either email or password is missing. render the page with error
            return render(request, 'account/register.html', {'err': True})
    else:
        err = False
        return render(request, 'account/register.html', {'err': err})


def dashboard(request):
    return render(request, 'account/dashboard.html')