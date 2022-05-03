from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.utils import timezone

class Classes(models.Model):
    number = models.CharField(max_length=20, default='№')
    content = models.TextField(blank=True, default='')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='photo')
    
    def __str__(self):
        return self.content