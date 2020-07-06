# Регистрируем тут таблички
from django.contrib import admin
from .models import Task  # Из файла models импортируем модель Task


admin.site.register(Task)  # Регистрируем модель Task
