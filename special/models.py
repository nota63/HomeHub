from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Special(models.Model):
    work = models.CharField(max_length=100)
    special = HTMLField()
    until = models.TextField()

    def __str__(self):
        return self.work
