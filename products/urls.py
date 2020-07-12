from django.conf.urls import url, include
from django.contrib import admin
from products import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('about', views.about, name='about'),
    # path('x', views.x),
    # url(r'^landing123/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]
