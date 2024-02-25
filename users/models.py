from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='first name')
    last_name = models.CharField(max_length=80, blank=True, null=True, verbose_name='last name')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='phone')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='city')
    avatar = models.ImageField(blank=True, null=True, verbose_name='avatar')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name='course')
