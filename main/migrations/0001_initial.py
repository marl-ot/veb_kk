# Generated by Django 4.0.3 on 2022-05-17 16:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=150, null=True, unique=True, verbose_name='Почта')),
                ('last_name', models.CharField(max_length=150, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=150, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DoneWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_work', models.ImageField(default='Готовая карта', upload_to='done_map/%Y/%m/%d/', verbose_name='Готовая работа')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('comment_from_student', models.CharField(default='Комментарий', max_length=255, verbose_name='Комментарий')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Идентификация студента')),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_num', models.IntegerField(default=1, verbose_name='Номер школы')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.ImageField(default='Базовая карта', upload_to='base_maps/%Y/%m/%d/', verbose_name='Работа')),
                ('legend', models.CharField(default='Легенда', max_length=255, verbose_name='Легенда')),
                ('task', models.CharField(default='Задание', max_length=255, verbose_name='Задание')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('comment_from_teacher', models.CharField(default='Комментарий', max_length=255, verbose_name='Комментарий')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_num', to=settings.AUTH_USER_MODEL, verbose_name='Идентификация студента')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='My_teacher', to=settings.AUTH_USER_MODEL, verbose_name='Учитель')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doneworks', verbose_name='Идентификация работы')),
            ],
        ),
        migrations.AddField(
            model_name='doneworks',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.works', verbose_name='Идентификация работы'),
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)], verbose_name='Номер Класса')),
                ('class_letter', models.CharField(default='буква', max_length=5, verbose_name='Буква класса')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.schools', verbose_name='Номер школы')),
            ],
        ),
        migrations.AddField(
            model_name='auth',
            name='full_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.classes', verbose_name='класс'),
        ),
        migrations.AddField(
            model_name='auth',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='auth',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
