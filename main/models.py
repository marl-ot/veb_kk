from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

class Classes(models.Model):
    number = models.CharField(max_length=20)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
