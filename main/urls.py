# Сами создали
# Отслеживание url адресов, легко поменять url-адрес

from django.urls import path
from . import views    # . - это значит из этой же директории

urlpatterns = [
    path('', views.index, name='home'),                 # Пустая строка - переход на главную страничку # В файле views функцию index
    path('about', views.about, name='about'),
    path('x', views.xxx)
    # можно ещё прописывать, '/' не нужно в начале
]