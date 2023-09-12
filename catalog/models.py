from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey
    price = models.DecimalField(verbose_name='Цена')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}/{self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
