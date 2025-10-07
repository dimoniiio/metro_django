from django.db import models


class Post(models.Model):
    "Класс описывающий пост"
    title = models.CharField("Название", max_length=255)
    content = models.TextField("Содержание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
