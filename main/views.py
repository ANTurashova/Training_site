# Если пользователь перешёл на то-то, то показываем то-то...
from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
from django.http import HttpResponse  # Чтобы выводить строку с текстом
from .models import Task  # Из этой директории из файла models импортирую класс Task
from .forms import TaskForm


def index(request):                                         # Обязательно получить параметр request
    tasks = Task.objects.order_by('-id')   # Получаем объекты таблички и сортируем от новых к старым # Срез пяти: [:5]
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})
                                                                      # Первым параметром request, вторым html-шаблон


def about(request):                                         # Обязательно получить параметр request
    return render(request, 'main/about.html')


def x(request):                                         # Обязательно получить параметр request
    return HttpResponse("<h4>X</h4>")


def create(request):
    error = ''
    if request.method == 'POST':  # Пропишет отслеживание из формы
        form = TaskForm(request.POST)
        if form.is_valid():  # Если полученные от пользователя данные коректны
            form.save()      # то обращается к форме к методу save, т.е. сохраняем
            return redirect('home')  # переадресовываем на страницу home
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {  # Словарь создадим отдельно, чтобы потом как переменную передать
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)