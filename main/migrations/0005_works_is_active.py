# Generated by Django 4.0.3 on 2022-05-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_schools_school_num_alter_works_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]
