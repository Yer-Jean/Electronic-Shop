# Generated by Django 4.2.5 on 2023-09-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Категория'),
        ),
    ]