import pytest
from ..models import Vote, Employee, Menu, Restaurant
from datetime import datetime
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


@pytest.mark.django_db
@pytest.fixture
def restaurant():
    restaurant = Restaurant.objects.create(
        name='abras',
        location='abras',
    )
    restaurant.save()
    return restaurant


@pytest.mark.django_db
@pytest.fixture
def menu(restaurant):
    menu = Menu.objects.create(
        id=1,
        restaurant=restaurant,
        date=datetime.now().date()
    )
    menu.save()
    return menu


@pytest.fixture
def url(menu):
    return reverse('create_vote', kwargs={'menu_id': menu.id})


@pytest.mark.django_db
def test_vote_success(client, user, url):

    data = {
        'score': 4
    }
    client.login(
       username='ser', password='12341234'
    )

    response = client.post(url, data=data)
    assert response.status_code == 200
    assert Vote.objects.count() == 1


@pytest.mark.django_db
def test_vote_unauthenticated(client, url):

    data = {
        'score': 4
    }

    response = client.post(url, data=data)
    assert response.status_code == 403
    assert Vote.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize(
   'score', [
       (0),
       (-1),
       (6),
   ]
)
def test_vote_invalid_score(client, user, url, score):
    data = {
        'score': score
    }
    client.login(
       username='ser', password='12341234'
    )

    response = client.post(url, data=data)
    assert response.status_code == 400
    assert Vote.objects.count() == 0


@pytest.mark.django_db
def test_vote_twice(client, user, url):

    data = {
        'score': 4
    }
    client.login(
       username='ser', password='12341234'
    )

    client.post(url, data=data)
    response = client.post(url, data=data)
    assert response.status_code == 400
    assert Vote.objects.count() == 1
