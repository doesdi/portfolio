from datetime import date

from django.db import models
from django.urls import reverse


class Items(models.Model):
    Grade = (
        ('Отлично!', 'Отлично!'),
        ('Очень хорошо', 'Очень хорошо'),
        ('Хорошо', 'Хорошо'),
        ('Плохо', 'Плохо'),
        ('Очень плохо', 'Очень плохо')
    )
    title = models.CharField(max_length=100, verbose_name="заголовок")
    name = models.CharField(max_length=100, verbose_name="имя")
    content = models.TextField(blank=True, verbose_name="текст")
    rating = models.CharField(max_length=15, choices=Grade, default='Отлично!', verbose_name="оценка")
    published = models.BooleanField(default=True, verbose_name="опубликован")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="время создания")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
        ordering = ['-time_create', 'title']




