import json

from django.core.management import BaseCommand

from users.models import User, Payment
from materials.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('materials_data.json', 'r', encoding='utf-8') as file:
            materials_data = json.load(file)
            for data in materials_data:
                if data['model'] == 'materials.course':
                    Course.objects.create(name=data['fields']['name'],
                                          preview=data['fields']['preview'],
                                          description=data['fields']['description'])
                if data['model'] == 'materials.lesson':
                    Lesson.objects.create(name=data['fields']['name'],
                                          description=data['fields']['description'],
                                          preview=data['fields']['preview'],
                                          video_link=data['fields']['video_link'],
                                          course=Course.objects.get(id=data['fields']['course']))

        with open('users_data.json', 'r', encoding='utf-8') as file:
            users_data = json.load(file)
            for data in users_data:
                if data['model'] == 'users.user':
                    User.objects.create(email=data['fields']['email'],
                                        first_name=data['fields']['first_name'],
                                        last_name=data['fields']['last_name'],
                                        phone=data['fields']['phone'],
                                        city=data['fields']['first_name'],
                                        avatar=data['fields']['first_name'])
                if data['model'] == 'users.payment':
                    Payment.objects.create(date=data['fields']['date'],
                                           paid_summ=data['fields']['paid_summ'],
                                           payment_method=data['fields']['payment_method'],
                                           paid_course=Course.objects.get(id=data['fields']['paid_course']),
                                           user_id=data['fields']['user_id'])
