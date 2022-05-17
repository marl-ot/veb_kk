from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Auth(AbstractUser):
    patronymic = models.CharField(verbose_name = 'Отчество', max_length=255)
    school_number = models.IntegerField(null=True, verbose_name = 'Номер школы', blank=True)
    birth_date = models.DateField(null=True, verbose_name = 'Дата рождения', blank=True)
    is_teacher = models.BooleanField(verbose_name = 'Учитель', default=False)


class Classes(models.Model):
    class_number = models.IntegerField(verbose_name = 'Номер Класса', validators=[MinValueValidator(1), MaxValueValidator(11)], default=1)
    class_letter = models.CharField(verbose_name = 'Буква класса', max_length=2, default="what's letter?")

    def __str__(self):
        return (str(self.class_number) + str(self.class_letter))

class Works(models.Model):
    work = models.ImageField(verbose_name = 'Работа', upload_to="base_maps/%Y/%m/%d/", default='base_map')
    legend = models.CharField(verbose_name = 'Легенда', max_length=255, default='text')
    task = models.CharField(verbose_name = 'Задание', max_length=255, default='text')

class DoneWorks(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Идентификация студента', on_delete = models.PROTECT)
    done_work = models.ImageField(verbose_name = 'Готовая работа', upload_to="done_map/%Y/%m/%d/", default='current_map')
    work = models.ForeignKey(Works, verbose_name = 'Идентификация работы', on_delete = models.CASCADE)
    time_create = models.DateTimeField(verbose_name = 'Время создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name = 'Время обновления', auto_now=True)


class Grades(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Идентификация студента', on_delete = models.PROTECT, related_name = 'student_num')
    work = models.ForeignKey(DoneWorks, verbose_name = 'Идентификация работы', on_delete = models.CASCADE)
    grade = models.IntegerField(verbose_name = 'Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Учитель', on_delete = models.CASCADE, related_name = 'My_teacher')

#class MyUser(AbstractBaseUser):


#school_number = models.CharField(max_length=30, blank=True)
