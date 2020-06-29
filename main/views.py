# Если пользователь перешёл на то-то, то показываем то-то...

from django.shortcuts import render
from django.http import HttpResponse                        # Чтобы выводить строку с текстом


def index(request):                                         # Обязательно получить параметр request
    return render(request, 'main/index.html')  # Первым параметром request, вторым html-шаблон


def about(request):                                         # Обязательно получить параметр request
    return render(request, 'main/about.html')


def xxx(request):                                         # Обязательно получить параметр request
    return HttpResponse("<h4>X</h4>")