import pytest
from datetime import date
from employees.models import Employer

@pytest.mark.django_db
def test_employer_age():
    employer = Employer(name="John Doe", birth_date=date(1994, 4, 8))
    assert employer.age == date.today().year - 1994 - (
        (date.today().month, date.today().day) < (4, 8)
    )
