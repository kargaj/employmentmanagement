from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_name(value):
    if len(value.split()) < 2:
        raise ValidationError("Name must contain at least two words (first and last name).")

def validate_birth_date(value):
    if value >= timezone.now().date():
        raise ValidationError("Birth date must be earlier than today.")
