# Эта формочка будет работать с моделью
from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):  # Название обычно дают по имени модели плюс Form
    class Meta:  # В Meta-классе можем указать доп. настройки
        model = Task  # Скажем, с какой моделью мы работаем
        fields = ["title", "task"]
        # Fiels это список, в котороом мы указываем, какие поля (из модели) должны присутсвоватьв самой формочке
        widgets = {  # Стили
            "title": TextInput(attrs={
                'class': 'ppp',
                'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'ppp',
                'placeholder': 'Введите описание'
            }),
        }