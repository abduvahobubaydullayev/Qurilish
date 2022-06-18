from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL

# Create your models here.


class Firm(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='media/firm_images/', blank=True, null=True)
    viloyat = models.CharField(max_length=120, blank=True, null=True)
    tuman = models.CharField(max_length=120, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    choices = [
        ['s', 'Sotuvchi'],
        ['h', 'Haridor'],
    ]
    image = models.ImageField(upload_to='media/user_images/', blank=True, null=True)
    auth = models.CharField(choices=choices, max_length=1, blank=True, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)


