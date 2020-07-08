# Регистрируем тут таблички
from django.contrib import admin
from .models import *  # Перед регистрацией из файла models импортируем все модели


class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]  # Какие поля мы хотим выводить
    list_display = [field.name for field in Subscriber._meta.fields]  # Вывести все поля
    # exclude = ["email"]  # на странице редактирования записи исключить поле
    # fields = ["email"]  # на страницк редактирования выводить только email
    # list_filter = ["name"]  # справа появились фильтры фильтровать по одинаковому имени
    # search_fields = ["name"]  # сверху появился поиск по имени
    search_fields = ["name", "email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)  # Регистрируем модель

