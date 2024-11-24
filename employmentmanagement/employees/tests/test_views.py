import pytest
from datetime import date
from rest_framework.test import APIClient
from rest_framework import status
from employees.models import Employee

@pytest.mark.django_db
def test_employee_list():
    client = APIClient()
    Employee.objects.create(name="John Doe", birth_date=date(1994, 4, 8), department="HR")
    Employee.objects.create(name="Jane Doe", birth_date=date(1994, 7, 31), department="DEV")
    response = client.get("/employees/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_create_employee():
    client = APIClient()
    data = {"name": "Alice Smith", "birth_date": "1994-04-13", "department": "HR"}
    response = client.post("/employees/", data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == "Alice Smith"