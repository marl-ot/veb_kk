# Generated by Django 4.0.3 on 2022-05-22 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_classes_teacher_alter_classes_class_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='teacher',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
    ]
