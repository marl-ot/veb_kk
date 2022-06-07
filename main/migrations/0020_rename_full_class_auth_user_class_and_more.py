# Generated by Django 4.0.3 on 2022-05-26 17:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_grades_student_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='full_class',
            new_name='user_class',
        ),
        migrations.AddField(
            model_name='doneworks',
            name='check_status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='doneworks',
            name='comment_from_teacher',
            field=models.CharField(blank=True, max_length=255, verbose_name='Комментарий от учителя'),
        ),
        migrations.AddField(
            model_name='doneworks',
            name='grade',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
        migrations.AddField(
            model_name='doneworks',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Учитель', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_letter',
            field=models.CharField(max_length=3, verbose_name='Буква класса'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)], verbose_name='Номер класса'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='doneworks',
            name='comment_from_student',
            field=models.CharField(blank=True, max_length=127, verbose_name='Комментарий от ученика'),
        ),
        migrations.AlterField(
            model_name='schools',
            name='school_num',
            field=models.IntegerField(unique=True, verbose_name='Номер школы'),
        ),
        migrations.AlterField(
            model_name='works',
            name='number',
            field=models.IntegerField(verbose_name='Номер задания'),
        ),
        migrations.AlterField(
            model_name='works',
            name='task',
            field=models.CharField(max_length=511, null=True, verbose_name='Задание'),
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
    ]