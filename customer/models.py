from django.db import models
from django.contrib.postgres.fields import CIEmailField

from core.fields import CustomPhoneNumberField
from core.models import TimestampModel


class Customer(TimestampModel):
    name = models.CharField(max_length=128)
    email = CIEmailField(unique=True)
    phone = CustomPhoneNumberField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128, db_index=True)


    class Meta:
        db_table = 'customer'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class PaymentType(models.TextChoices):
        CASH = 'cash'
        CHEQUE = 'cheque'
        CREDIT_CARD = 'credit card'
        BANK_TRANSFER = 'bank transfer'
        BANK_DEPOSIT = 'bank deposit'


class CustomerPayment(TimestampModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    payment_type = models.CharField(max_length=128, choices=PaymentType.choices)
    ref_code = models.CharField(max_length=128)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer_payment'
        ordering = ('-id',)

    def __str__(self):
        return self.ref_code
