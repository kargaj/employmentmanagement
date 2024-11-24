import pytest
from datetime import date
from employees.models import Employee
from employees.serializers import EmployeeSerializer

@pytest.mark.django_db
def test_employee_serializer():
    employee = Employee.objects.create(name="Jane Doe", birth_date=date(1994, 4, 8), department="HR")
    
    serializer = EmployeeSerializer(employee)
    assert serializer.data == {
        "id": employee.id,
        "name": "Jane Doe",
        "birth_date": "1994-04-08",
        "department": "HR",
        "department_fullname": "Human Resources",
        "age": employee.age,
    }
