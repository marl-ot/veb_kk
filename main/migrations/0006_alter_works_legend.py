# Generated by Django 4.0.3 on 2022-05-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_works_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='legend',
            field=models.CharField(default='Легенда', max_length=511, verbose_name='Легенда'),
        ),
    ]