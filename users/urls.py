from django.urls import path

from users.views import UserUpdateAPIView, PaymentListAPIView, UserRetrieveAPIView

app_name = 'users'

urlpatterns = [
    path('profile/update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),
    path('profile/<int:pk>/', UserRetrieveAPIView.as_view(), name='profile_detail'),

    path('payment/', PaymentListAPIView.as_view(), name='payment'),
]
