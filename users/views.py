from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
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
