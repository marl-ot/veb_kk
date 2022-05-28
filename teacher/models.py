from django.db import models

""" 
class Atlasses(models.Model):
    atlas_year = models.IntegerField(verbose_name = 'Год издания атласа', null=True)
    page_number = models.IntegerField(verbose_name = 'Номер страницы', null=True)
    atlas_name = models.CharField(verbose_name = 'Название атласа', max_length=255, unique=True)
    atlas_author = models.CharField(verbose_name = 'ФИО автора', max_length=255, unique=True)
    picture_of_page = models.ImageField(
        verbose_name = 'Изображение страницы', 
        upload_to="atlas/%Y/", 
        default='Готовая карта'
    )

    def __str__(self):
        return str(self.atlas_name)
"""
