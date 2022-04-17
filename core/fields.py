from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python
from rest_framework.exceptions import ValidationError

from .validators import validate_phone_number


class CustomPhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_phone_number]

    def to_internal_value(self, data):
        phone_number = to_python(data)
        if phone_number and not phone_number.is_valid():
            raise ValidationError(self.error_messages["invalid"])
        return phone_number.as_e164
