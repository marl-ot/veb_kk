# Generated by Django 4.0.3 on 2022-05-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_auth_email_alter_auth_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='email',
            field=models.EmailField(max_length=150, null=True, unique=True, verbose_name='Почта'),
        ),
    ]
