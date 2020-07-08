# Описание полей в таблице БД
from django.db import models  # Без неё не можем обращаться к models


class Subscriber(models.Model):  # Имя Task любое, наследуем всё от models от его класса Model
    email = models.EmailField()  # Поле для email
    name = models.CharField(max_length=128)  # Поле текстовое до 255 символов, обязательно параметр длины!

    def __str__(self):  # Для того, чтобы таблички в админке презентовали желаемые подписи
        # return self.id  # Презентует id. self - запись из этой модели
        # return self.email
        return "%s - %s" % (self.name, self.email)  # Презентует и мэйл, и имя

    class Meta:  # Переименовать модель в админке
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
