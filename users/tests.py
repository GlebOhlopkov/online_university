from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course
from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="test@mail.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='test')

    def test_retrieve_subscribe(self):
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(
            '/users/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
