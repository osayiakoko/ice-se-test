from rest_framework.viewsets import ModelViewSet

from ..filters import CustomerFilter, CustomerPaymentFilter
from ..models import Customer, CustomerPayment
from .serializers import CustomerPaymentSerializer, CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class CustomerPaymentViewSet(ModelViewSet):
    queryset = CustomerPayment.objects.select_related('customer')
    serializer_class = CustomerPaymentSerializer
    filterset_class = CustomerPaymentFilter
