from django_filters import rest_framework as filters

from .models import Customer, CustomerPayment


class CustomerFilter(filters.FilterSet):
    state = filters.CharFilter(field_name="state", lookup_expr='iexact')

    class Meta:
        model = Customer
        fields = ['state']


class CustomerPaymentFilter(filters.FilterSet):
    customer_id = filters.NumberFilter(field_name='customer_id')
    amount_gt = filters.NumberFilter(field_name='amount', lookup_expr='gt')
    amount_lt = filters.NumberFilter(field_name='amount', lookup_expr='lt')

    class Meta:
        model = CustomerPayment
        fields = [
            'customer_id', 
            'amount_gt',
            'amount_lt',
        ]
