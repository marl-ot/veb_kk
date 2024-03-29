#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser #AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
#from django.urls import reverse
#from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
#from django.contrib.auth.models import UserManager
#from django.db.models.signals import post_save
#from django.dispatch import receiver


class Schools(models.Model):
    school_num = models.IntegerField(verbose_name = 'Номер школы', unique=True)

    school_name = models.CharField(
        null=True, 
        verbose_name = 'Название школы', 
        max_length=150, 
        default = 'ГБОУ', 
        blank=True
    )

    def __str__(self):
        return ('№' + str(self.school_num))

    class Meta:
        verbose_name = _("schools")
        verbose_name_plural = _("Школы")


class Classes(models.Model):
    class_number = models.IntegerField(
        verbose_name = 'Номер класса', 
        validators=[MinValueValidator(1), MaxValueValidator(11)],
        blank = False
    )
    class_letter = models.CharField(verbose_name = 'Буква класса', max_length=3, blank = False)
    school = models.ForeignKey(Schools, null=True, verbose_name = 'Номер школы', on_delete = models.CASCADE, blank = False)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name = 'Учитель', 
        on_delete = models.PROTECT,
        blank = False
    )

    def __str__(self):
        return (str(self.class_number) + str(self.class_letter) + ' №' + str(self.school.school_num))

    class Meta:
        verbose_name = _("classes")
        verbose_name_plural = _("Классы")


class Auth(AbstractUser):
    email = models.EmailField(null=True, verbose_name = 'Почта', unique=True, max_length=150)
    last_name = models.CharField(null=True, verbose_name = 'Фамилия', max_length=150)
    first_name = models.CharField(null=True, verbose_name = 'Имя', max_length=150)
    patronymic = models.CharField(null=True, verbose_name = 'Отчество', max_length=150)
    birth_date = models.DateField(null=True, verbose_name = 'Дата рождения', blank=True)
    is_teacher = models.BooleanField(verbose_name = 'Учитель', default=False)
    user_class = models.ForeignKey(
        Classes, 
        null=True,
        verbose_name = 'Класс', 
        on_delete = models.CASCADE, 
        blank=True
    )
    school_number = models.ForeignKey(
        Schools, 
        null=True, 
        verbose_name = 'Номер школы', 
        on_delete = models.CASCADE
    )

    def __str__(self):
        if self.is_teacher:
            return ('Учитель ' + str(self.last_name) + ' ' + str(self.first_name) + ' ' + str(self.patronymic))
        else:
            return (str(self.username))

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("Пользователи")


class Works(models.Model):
    number = models.IntegerField(verbose_name = 'Номер задания', blank = False)
    work = models.ImageField(
        verbose_name = 'Работа',
        upload_to="base_maps/%Y/%m/", 
        default='Базовая карта'
    )
    legend = models.CharField(verbose_name = 'Условные обозначения', max_length=511, blank = True)
    task = models.CharField(null=True, verbose_name = 'Задание', max_length=511)
    school_number = models.ForeignKey(
        Schools, 
        null=True, 
        verbose_name = 'Номер школы', 
        on_delete = models.CASCADE
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name = 'Учитель', 
        on_delete = models.PROTECT, 
        blank=False,
        default=2
    )
    for_class = models.ForeignKey(
        Classes, 
        null=True,
        verbose_name = 'Класс', 
        on_delete = models.CASCADE
    )
    is_active = models.BooleanField(verbose_name = "Активность", default=False)
    work_name = models.CharField(verbose_name = 'Название задания', max_length=50, blank = False)

    def __str__(self):
        return (str(self.work_name) + ' ' + str(self.school_number.school_num))
        
    class Meta:
        verbose_name = _("works")
        verbose_name_plural = _("Заданные работы")


class DoneWorks(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name = 'Идентификация студента', 
        on_delete = models.PROTECT
    )
    done_work = models.ImageField(
        verbose_name = 'Готовая работа', 
        upload_to="done_map/%Y/%m/%d/", 
        default='Готовая карта'
    )
    work = models.ForeignKey(Works, verbose_name = 'Идентификация работы', on_delete = models.CASCADE)
    grade = models.IntegerField(null=True, verbose_name = 'Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    check_status = models.BooleanField(verbose_name = 'Статус', default=False)
    time_create = models.DateTimeField(verbose_name = 'Время создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name = 'Время обновления', auto_now=True)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,  
        verbose_name = 'Учитель', 
        on_delete = models.PROTECT, 
        related_name = 'Учитель'
    )
    comment_from_teacher = models.CharField(
        verbose_name = 'Комментарий от учителя', 
        null=True,
        max_length=255,
        blank=True,
    )
    comment_from_student = models.CharField(
        verbose_name = 'Комментарий от ученика',
        null=True,
        max_length=127,
        blank=True,
    )

    def __str__(self):
        return (str(self.student.last_name) + ' ' + str(self.work.work_name) + ' оценка ' + str(self.grade))

    class Meta:
        verbose_name = _("done_works")
        verbose_name_plural = _("Сделанные работы")
