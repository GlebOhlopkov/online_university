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


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("CASH", "paid by cash"),
        ("CARD", "paid by card"),
    ]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='user')
    date = models.DateField(verbose_name='date')
    paid_course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='paid_course')
    paid_summ = models.FloatField(verbose_name='paid_summ')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='paid_type')
