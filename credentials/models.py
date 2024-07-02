from django.db import models


# Create your models here.

class Credentials(models.Model):
    admin_username = models.CharField(max_length=400)
    admin_password = models.CharField(max_length=400)
    unique_password = models.CharField(max_length=400)

    def __str__(self):
        return self.admin_username
