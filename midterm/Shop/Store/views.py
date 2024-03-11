from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *

from .models import *


# Create your views here.

def homepage(request):
    Products = Product.objects.get_all_products()
    return render(request, 'Store/productList.html', {'Products': Products})


def get_pr_by_cat(request, cat_id):
    Products = Product.objects.get_cat_pr(cat_id)
    return render(request, 'Store/productList.html', {'Products': Products})

def busket(request):
    return render(request, 'Store/busket.html')

def purch(request):
    return render(request, 'Store/purchases.html')

def profil(request):
    return render(request, 'Store/profil.html')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'Store/login.html'

    def get_success_url(self):
        return reverse_lazy('home')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'Store/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def add_Buscket(request, product, amount):
    if request.user.is_authenticated():
        pr = product
        am = amount
        us = request.user.pk

        b = BusketItems.objects.create(product = pr, amount=am, user=us)
        b.save()

