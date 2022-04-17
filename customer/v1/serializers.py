from rest_framework import serializers
from core.constants import NG_STATES
from ..models import Customer, CustomerPayment


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_state(self, value):
        if value.title() not in NG_STATES:
            raise serializers.ValidationError('Invalid NG state')
        return value.title()


class CustomerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayment
        fields = '__all__'
