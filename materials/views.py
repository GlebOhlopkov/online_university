from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.paginators import MyPagePagination
from materials.permissions import IsModerator, IsOwner
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from materials.services import create_url_stripe_sessions
from payments.models import Payment


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPagePagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ('destroy',):
            self.permission_classes = [IsAuthenticated, ~IsModerator & IsOwner]
        elif self.action in ('list', 'update', 'partial_update', 'retrieve'):
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        return super().get_permissions()


class PaymentCourseAPIView(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data['course']
        try:
            course_item = get_object_or_404(Course, pk=course_id)
            url_payment_data = create_url_stripe_sessions(course_item)
            massage = 'Url for paid create'
            payment_data = {
                'user': user,
                'date': '2024-01-01',
                'paid_course': course_item,
                'paid_summ': course_item.price,
                'payment_method': 'CARD',
                'success_url': url_payment_data['url'],
                'services_id': url_payment_data['id'],
            }
            payment = Payment.objects.create(**payment_data)
            payment.save()
            return Response({'massage':massage, 'url': url_payment_data['url']})
        except:
            massage = 'Wrong course ID'
            return Response({'massage': massage})


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ]  # IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ]  # IsModerator]
    pagination_class = MyPagePagination

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
