from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
from .forms import SubscriberForm  # Из этой директории из файла models импортирую класс
from products.models import *


def index(request):                                         # Обязательно получить параметр request
    myname = "Великое Имя"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # print(form)
        # print(request.POST)
        print("----------")
        # print(form.cleaned_data)
        print(form.cleaned_data["name"])

        new_form = form.save()

    return render(request, 'test_store/index.html', locals())
    # Первым параметром request, вторым html-шаблон, locals() чтоб переменные ушли в html


def home(request):
    # products = Product.objects.filter(is_active=True)
    # Создаём переменные, чтобы прогнать их и вывести все товары. Выводим только активные.
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # products_images_phones = products_images.filter(product__category__id=1)
    # products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'test_store/home.html', locals())
