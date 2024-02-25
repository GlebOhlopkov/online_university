from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, \
    UserDeleteAPIView, SubscriptionAPIView

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),

    path('subscription/', SubscriptionAPIView.as_view(), name='subscription')
]
