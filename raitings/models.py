from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Articles(models.Model):
    surname = models.CharField('Фамилия', max_length = 50)
    name = models.CharField('Имя', max_length = 50)
    patronymic = models.CharField('Отчество', max_length = 50)
    task = models.CharField('Задание', max_length = 200)
    estimation = models.IntegerField('Оценка', validators=[MinValueValidator(2), MaxValueValidator(5)])

    def __str__(self):
        return self.surname
    
    def get_absolute_url(self):
        return f'/raitings/{self.id}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'