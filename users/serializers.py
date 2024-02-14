from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_payments = PaymentSerializer(source='payment_set.all', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'city', 'avatar', 'user_payments']
