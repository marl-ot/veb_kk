# Generated by Django 4.0.3 on 2022-05-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_works_work_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='work',
            field=models.ImageField(default='Базовая карта', upload_to='base_maps/%Y/%m/', verbose_name='Работа'),
        ),
    ]