from django.db import models
from django.utils import timezone

from .validators import validate_birth_date, validate_name


class Employer(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('DEV', 'Developers'),
        ('S&M', 'Sales&Marketing'),
    ]

    name = models.CharField(max_length=255, validators=[validate_name])
    birth_date = models.DateField(validators=[validate_birth_date])
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default=None, null=True, blank=True)


    @property
    def age(self):
        """Calculate age based on birth_date."""
        today = timezone.now().date()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
