import pytest
from datetime import date
from employees.models import Employee

@pytest.mark.django_db
def test_employee_age():
    employee = Employee(name="John Doe", birth_date=date(1994, 4, 8))
    assert employee.age == date.today().year - 1994 - (
        (date.today().month, date.today().day) < (4, 8)
    )
