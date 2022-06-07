# Generated by Django 4.0.3 on 2022-05-28 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_full_class_auth_user_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='for_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.classes', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='works',
            name='legend',
            field=models.CharField(blank=True, max_length=511, verbose_name='Условные обозначения'),
        ),
    ]