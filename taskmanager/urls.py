from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

admin.autodiscover()  # Джанго находит автоматически все файлы admin.py


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main/', include('main.urls')),                             # Пустая строка - переход на главную страничку
    path('', include('test_store.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^', include('test_store.urls')),
    # url(r'^', include('products.urls')),
    # url(r'^', include('orders.urls')),
]
