# Регистрируем тут таблички
from django.contrib import admin
from .models import *  # Перед регистрацией из файла models импортируем все модели


class ProductInOrderInline(admin.TabularInline):
    model = ProductImage  # чтобы вложить фотографии на странице редактирования товара
    extra = 0  # чтобы не было допонительных рядов с пустыми картинками


class ProductImageInline(admin.TabularInline):
    model = ProductImage  # чтобы вложить фотографии на странице редактирования товара
    extra = 0  # чтобы не было допонительных рядов с пустыми картинками


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # Вывести все поля
    inlines = [ProductImageInline]  # чтобы вложить фотографии на странице редактирования товара

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)  # Регистрируем модель


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # Вывести все поля

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)  # Регистрируем модель

