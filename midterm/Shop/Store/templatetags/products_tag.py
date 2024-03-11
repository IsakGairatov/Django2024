from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('Store/cat_list.html')
def ShowCats():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('Store/menu.html')
def ShowMenu(isLoged):
    if isLoged == 1:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Войти', 'link': 'login'}]
    else:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Моя Корзина', 'link': 'busket'}, {'title': 'Мои Покупки', 'link': 'purchases'}]
    return {'menu': menu}