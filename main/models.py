from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.utils import timezone

class Classes(models.Model):
    number = models.CharField(max_length=20, default='№')
    content = models.TextField(blank=True, default='')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='photo')
    
    def __str__(self):
        return self.content