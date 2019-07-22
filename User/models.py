from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username