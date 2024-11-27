import pytest
from datetime import date
from employees.models import Employer
from employees.serializers import EmployerSerializer

@pytest.mark.django_db
def test_employee_serializer():
    employer = Employer.objects.create(name="Jane Doe", birth_date=date(1994, 4, 8), department="HR")
    
    serializer = EmployerSerializer(employer)
    assert serializer.data == {
        "id": employer.id,
        "name": "Jane Doe",
        "birth_date": "1994-04-08",
        "department": "HR",
        "department_fullname": "Human Resources",
        "age": employer.age,
    }
