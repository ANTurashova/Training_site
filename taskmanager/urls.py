from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()  # Джанго находит автоматически все файлы admin.py


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main/', include('main.urls')),                             # Пустая строка - переход на главную страничку
    path('', include('test_store.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
