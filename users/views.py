from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import User, Subscription
from users.permissions import IsOwnerYourself
from users.serializers import UserSerializer, UserHideSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerYourself]

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class1 = UserSerializer
    serializer_class2 = UserHideSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object():
            self.serializer_class = self.serializer_class2
            return super().retrieve(request, *args, **kwargs)
        else:
            self.serializer_class = self.serializer_class1
            return super().retrieve(request, *args, **kwargs)


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerYourself]


class SubscriptionAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = int(self.request.data.get('course'))
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item).all()
        if subs_item.exists():
            subs_item.delete()
            message = 'Subscription delete'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Subscription create'
        return Response({"message": message})
