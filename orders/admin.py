# Регистрируем тут таблички в админке 
from django.contrib import admin
from .models import *  # Перед регистрацией из файла models импортируем все модели


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder  # чтобы вложить фотографии на странице редактирования товара
    extra = 0  # чтобы не было допонительных рядов с пустыми картинками


class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # Вывести все поля
   
    class Meta:
        model = Status
        
        
admin.site.register(Status, StatusAdmin)  # Регистрируем модель


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]  # Вывести все поля
    inlines = [ProductInOrderInline]  # чтобы вложить товары на странице редактирования заказа

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)  # Регистрируем модель


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]  # Вывести все поля

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)  # Регистрируем модель

