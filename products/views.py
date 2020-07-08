# from django.shortcuts import render, redirect  # redirect поможет перевести пользователя на другую страницу
# from django.http import HttpResponse  # Чтобы выводить строку с текстом
# # from .forms import SubscriberForm  # Из этой директории из файла models импортирую класс
#

# def index(request):                                         # Обязательно получить параметр request
#     myname = "Великое Имя"
#     form = SubscriberForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         # print(form)
#         # print(request.POST)
#         print("----------")
#         # print(form.cleaned_data)
#         print(form.cleaned_data["name"])
#
#         new_form = form.save()
#
#     return render(request, 'test_store/index.html', locals())
#     # Первым параметром request, вторым html-шаблон, locals() чтоб переменные ушли в html
#
#
# def about(request):                                         # Обязательно получить параметр request
#     return render(request, 'main/about.html')
#
#
# def x(request):                                             # Обязательно получить параметр request
#     return HttpResponse("<h4>X</h4>")
#
