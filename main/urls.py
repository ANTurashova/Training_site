# Сами создали
# Отслеживание url адресов

from django.urls import path
from . import views # . - это значит из этой же директории

urlpatterns = [
    path('', views.index),                 # Пустая строка - переход на главную страничку # В файле views функцию index
    path('about-us', views.about),
    path('x', views.xxx)
    # можно ещё прописывать, '/' не нужно в начале
]