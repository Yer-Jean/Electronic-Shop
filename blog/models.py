from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    slug = models.CharField(max_length=200, verbose_name='Слог')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title} {self.views_count}'

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('-created_at',)
