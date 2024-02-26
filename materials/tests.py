from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from materials.models import Course, Lesson
from users.models import User
from rest_framework.test import force_authenticate


class CourseAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='testuser@mail,com',
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='testcourse1',
            description='testdescription1',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='testlesson1',
            description='testdescription1',
            video_link='youtube.com',
            course=self.course,
            owner=self.user
        )

    def test_get_list_course(self):
        response = self.client.get(reverse('materials:course-list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_list_lesson(self):
        response = self.client.get(reverse('materials:lesson_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {
            'name': 'testlesson2',
            'description': 'testdescription2',
            'course': 1,
            'owner': 1,
            'video_link': 'https://youtube.com',
        }
        response = self.client.post(
            '/materials/lesson/create/',
            data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        response = self.client.delete('/materials/lesson/delete/3/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_update_lesson(self):
        data = {
            'name': 'test',
            'description': 'test'
        }
        response = self.client.patch(
            '/materials/lesson/update/6/',
            data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def tearDown(self):
        pass
