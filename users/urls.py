from django.urls import path

from users.views import UserUpdateAPIView

app_name = 'users'

urlpatterns = [
    path('profile/update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),
]
