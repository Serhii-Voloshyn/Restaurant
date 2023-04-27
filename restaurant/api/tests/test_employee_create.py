import pytest
from django.test import Client
from ..models import Employee
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
   'email, password, username, status_code, count', [
       ('', '', '', 400, 0),
       ('', '1234abras', 'username', 400, 0),
       ('user@example.com', '', 'username', 400, 0),
       ('user@example.com', '1234', 'username', 400, 0),
       ('user@example.com', '1234abras', 'username', 201, 1),
   ]
)
def test_create_employee(
   email, password, status_code, username, count, client
):
    url = reverse('create_employee')
    data = {
        'username': username,
        'email': email,
        'password': password,
        'first_name': 'ser',
        'last_name': 'ser'
    }
    response = client.post(url, data=data)
    assert response.status_code == status_code
    assert len(Employee.objects.all()) == count
    if count:
        assert Employee.objects.get(email=email).password != password


@pytest.mark.django_db
def test_email_exists(client):
    Employee.objects.create_user(
        username='ser',
        email='ser@gmail.com',
        password='12341234',
        first_name='ser',
        last_name='ser'
    )
    url = reverse('create_employee')
    data = {
        'username': 'ser1',
        'email': 'ser@gmail.com',
        'password': '12341234',
        'first_name': 'ser',
        'last_name': 'ser'
    }
    response = client.post(url, data=data)
    assert response.status_code == 400
    assert len(Employee.objects.all()) == 1


@pytest.mark.django_db
def test_username_exists(client):
    Employee.objects.create_user(
        username='ser',
        email='ser@gmail.com',
        password='12341234',
        first_name='ser',
        last_name='ser'
    )
    url = reverse('create_employee')
    data = {
        'username': 'ser',
        'email': 'ser1@gmail.com',
        'password': '12341234',
        'first_name': 'ser',
        'last_name': 'ser'
    }
    response = client.post(url, data=data)
    assert response.status_code == 400
    assert len(Employee.objects.all()) == 1
