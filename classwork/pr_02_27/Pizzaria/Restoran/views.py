from django.shortcuts import render
from .models import *
# Query sets

All_food = Food.objects.all()
All_cat = Category.objects.all()