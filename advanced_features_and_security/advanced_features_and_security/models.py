from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(models.Manager):
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