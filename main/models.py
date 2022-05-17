#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser #AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
#from django.urls import reverse
#from django.utils import timezone
from django.conf import settings
#from django.contrib.auth.models import UserManager
#from django.db.models.signals import post_save
#from django.dispatch import receiver

"""
class IsTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'isteacher')
    patronymic = models.CharField(verbose_name = 'Отчество', max_length=255)
    school_number = models.CharField(max_length=30, verbose_name = 'Номер школы', blank=True)
    birth_date = models.DateField(null=True, verbose_name = 'Дата рождения', blank=True)
    is_teacher = models.BooleanField(verbose_name = 'Учитель', default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        IsTeacher.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.isteacher.save()
"""


class Schools(models.Model):
    school_num = models.IntegerField(verbose_name = 'Номер школы', default=1)


class Classes(models.Model):
    class_number = models.IntegerField(verbose_name = 'Номер Класса', validators=[MinValueValidator(1), MaxValueValidator(11)], default=1)
    class_letter = models.CharField(verbose_name = 'Буква класса', max_length=5, default="буква")
    full_class = (str(class_number) + str(class_letter))
    school = models.ForeignKey(Schools, null=True, verbose_name = 'Номер школы', on_delete = models.CASCADE)

    def __str__(self):
        return (str(self.class_number) + str(self.class_letter))

class Auth(AbstractUser):
    email = models.EmailField(null=True, verbose_name = 'Почта', unique=True, max_length=150)
    last_name = models.CharField(null=True, verbose_name = 'Фамилия', max_length=150)
    first_name = models.CharField(null=True, verbose_name = 'Имя', max_length=150)
    patronymic = models.CharField(null=True, verbose_name = 'Отчество', max_length=150)
    birth_date = models.DateField(null=True, verbose_name = 'Дата рождения', blank=True)
    is_teacher = models.BooleanField(verbose_name = 'Учитель', default=False)
    full_class = models.ForeignKey(Classes, null=True, verbose_name = 'класс', on_delete = models.CASCADE)
    
class Works(models.Model):
    work = models.ImageField(verbose_name = 'Работа', upload_to="base_maps/%Y/%m/%d/", default='Базовая карта')
    legend = models.CharField(verbose_name = 'Легенда', max_length=255, default='Легенда')
    task = models.CharField(verbose_name = 'Задание', max_length=255, default='Задание')

class DoneWorks(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Идентификация студента', on_delete = models.PROTECT)
    done_work = models.ImageField(verbose_name = 'Готовая работа', upload_to="done_map/%Y/%m/%d/", default='Готовая карта')
    work = models.ForeignKey(Works, verbose_name = 'Идентификация работы', on_delete = models.CASCADE)
    time_create = models.DateTimeField(verbose_name = 'Время создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name = 'Время обновления', auto_now=True)
    comment_from_student = models.CharField(verbose_name = 'Комментарий', max_length=255, default='Комментарий')


class Grades(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Идентификация студента', on_delete = models.PROTECT, related_name = 'student_num')
    work = models.ForeignKey(DoneWorks, verbose_name = 'Идентификация работы', on_delete = models.CASCADE)
    grade = models.IntegerField(verbose_name = 'Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Учитель', on_delete = models.PROTECT, related_name = 'My_teacher')
    comment_from_teacher = models.CharField(verbose_name = 'Комментарий', max_length=255, default='Комментарий')

#school_number = models.CharField(max_length=30, blank=True)
