import pytest
import requests
from faker import Faker

from . import endpoints
from .models import random_city_body, random_mountain_body, random_river_body

fake = Faker()


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture()
def sample_city(request):
    body = random_city_body()
    response = requests.post(endpoints.city_list, json=body)
    assert response.status_code == 201
    city_id = response.json()['id']

    def delete_city():
        requests.delete(endpoints.city_with_id(city_id))

    request.addfinalizer(delete_city)

    return body['name'], body['population'], city_id


@pytest.fixture()
def sample_mountain(request):
    body = random_mountain_body()
    response = requests.post(endpoints.mountain_list, json=body)
    assert response.status_code == 201
    mountain_id = response.json()['id']

    def delete_mountain():
        requests.delete(endpoints.mountain_with_id(mountain_id))

    request.addfinalizer(delete_mountain)

    return body['name'], body['height'], mountain_id


@pytest.fixture()
def sample_river(request):
    body = random_river_body()
    response = requests.post(endpoints.river_list, json=body)
    assert response.status_code == 201
    river_id = response.json()['id']

    def delete_river():
        requests.delete(endpoints.river_with_id(river_id))

    request.addfinalizer(delete_river)

    return body['name'], body['length'], river_id
