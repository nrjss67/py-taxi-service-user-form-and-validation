from django.core.exceptions import ValidationError


class LicenseNumberValidator:
    def __call__(self, value):
        if not len(value) == 8:
            raise ValidationError("Invalid license number")
        if not value[:3].isupper() or not value[3:].isdigit():
            raise ValidationError("Invalid license number")
        return value

    def deconstruct(self):
        return (f"taxi.validators.{self.__class__.__name__}",
                [],
                {})
