# Generated by Django 4.2.5 on 2023-10-11 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('-num',), 'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
    ]