from rest_framework import serializers

from payments.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_payments = PaymentSerializer(source='payment_set.all', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'city', 'avatar', 'user_payments']


class UserHideSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'phone', 'city', 'avatar',]
