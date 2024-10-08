from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth, profile_photo, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('date_of_birth', date_of_birth)
        extra_fields.setdefault('profile_photo', profile_photo)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, date_of_birth, profile_photo, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('date_of_birth', date_of_birth)
        extra_fields.setdefault('profile_photo', profile_photo)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=False, null=False)
    profile_photo = models.ImageField(blank=False)

    objects = CustomUserManager()



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=False, null=False)
    profile_photo = models.ImageField(blank=False)

    objects = CustomUserManager()

    class Meta:
        "can_create", "can_delete"
        permissions = [
            ("can_view", "Can view custom user"),
            ("can_create", "Can create custom user"),
            ("can_edit", "Can edit custom user"),
            ("can_delete", "Can delete custom user"),
        ]

# admin.py

from django.contrib import admin
from django.contrib.auth.models import Group, Permission

admin.site.register(Group)
admin.site.register(Permission)