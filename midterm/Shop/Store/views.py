import logging

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
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
    b = BusketItems.objects.get_UserBusket(request.user.pk).get_not_purchased()
    total_cost = 0

    for i in b:
        total_cost += i.product.cost * i.amount


    return render(request, 'Store/busket.html', {'busket' : b, 'total_cost': total_cost})

def purch(request):
    b = BusketItems.objects.get_UserBusket(request.user.pk).get_purchased()
    return render(request, 'Store/purchases.html', {'busket': b})

def profil(request):
    us = UserInfo.objects.get(user=request.user)
    return render(request, 'Store/profil.html', {'me': us})

def addAdress(request):
    if request.method == 'POST':
        form = addAdressForm(request.POST)
        if form.is_valid():
            try:
                form.instance.user = request.user
                Adress.objects.get(user=request.user).delete()
                form.save()
                ui = UserInfo.objects.get(user=request.user)
                ui.default_address = Adress.objects.get(user=request.user)
                ui.save()
                return redirect('profil')
            except:
                form.add_error(None, 'Ошибка')
    else:
        form = addAdressForm()
    return render(request, 'Store/addAdress.html', {'form': form})

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
        UserInfo.objects.just_registrated(user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')



def add_Buscket(request, pr, am):
    previous_page_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        BusketItems.objects.addItem(pr, am, request.user)
        return redirect(previous_page_url)

    else: return redirect(previous_page_url)

def del_Buscket(request, id):
    previous_page_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        BusketItems.objects.get(pk=id).delete()
        return redirect(previous_page_url)


def buy_Buscket(request):
    previous_page_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:

        return redirect(previous_page_url)


