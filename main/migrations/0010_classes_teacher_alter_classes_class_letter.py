# Generated by Django 4.0.3 on 2022-05-22 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_works_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_letter',
            field=models.CharField(default=' ', max_length=3, verbose_name='Буква класса'),
        ),
    ]
