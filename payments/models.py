from django.db import models


from materials.models import Course, Lesson
from users.models import User


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("CASH", "paid by cash"),
        ("CARD", "paid by card"),
    ]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='user')
    date = models.DateTimeField(verbose_name='date')
    paid_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.DO_NOTHING,
                                    verbose_name='paid_course')
    paid_lesson = models.ForeignKey(Lesson, blank=True, null=True, on_delete=models.DO_NOTHING,
                                    verbose_name='paid_lesson')
    paid_summ = models.FloatField(verbose_name='paid_summ')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='paid_type')
