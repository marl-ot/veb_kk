# Generated by Django 4.0.3 on 2022-05-23 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_grades_comment_from_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.classes', verbose_name='Класс'),
        ),
    ]
