import pytest
from ..models import Restaurant, Employee
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.fixture
def user():
    user = Employee.objects.create_user(
        username='ser',
        email='ser@gmail.com',
        password='12341234',
        first_name='ser',
        last_name='ser'
    )

    return user


@pytest.fixture
def url():
    return reverse('create_restaurant')


@pytest.mark.django_db
def test_create_restaurant_unauthenticated(client, url):

    data = {
        'name': 'abras',
        'location': 'abras'
    }

    response = client.post(url, data=data)
    assert response.status_code == 403
    assert Restaurant.objects.count() == 0


@pytest.mark.django_db
def test_create_restaurant_success(client, url, user):

    data = {
        'name': 'abras',
        'location': 'abras'
    }

    client.login(
       username='ser', password='12341234'
    )

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert Restaurant.objects.count() == 1
