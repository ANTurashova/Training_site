# отслеживание url адресов

from django.contrib import admin
from django.urls import path, include                                                        # Подключаем ещё и include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))                                       # Пустая строка - переход на главную страничку
]