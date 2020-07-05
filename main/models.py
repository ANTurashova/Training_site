# Всяк таблички БД
# Чтобы создать таблички, нам надо здесь создать новый класс
from django.db import models # Без неё не можем обращаться к models


class Task(models.Model):                                     # Имя Task, наследуем всё от models от его класса Model
    title = models.CharField('Название', max_length=50)       # CharField для текста до 255 символов
    task = models.TextField('Описание')                       # TextField для больших текстов

    def __str__(self):    # Метод, который вызывается тогда, когда мы выводим на экран объект этого класса
        return self.title