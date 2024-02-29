from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import Subscription, User
import datetime


@shared_task
def send_mail_for_course_update(course_id):
    sub = Subscription.objects.filter(course=course_id)
    user = sub[0].user
    course = sub[0].course
    send_mail(
        subject=f'{course} updated',
        message=f'{course} updated',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user]
    )


@shared_task
def deactivate_user():
    user_list = User.objects.all()
    date_now = datetime.date.today()
    deactivate_time = datetime.timedelta(days=30)
    for user in user_list:
        if date_now - user.last_login > deactivate_time:
            user.is_active = False
