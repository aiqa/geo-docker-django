from random import randint

import pytest
from faker import Faker

from ..models import City, Mountain, River

fake = Faker()


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture()
def sample_city():
    name, population = fake.city(), randint(300, 5_000_000)
    city = City.objects.create(name=name, population=population)
    return name, population, city.pk


@pytest.fixture()
def sample_mountain():
    name, height = fake.word(), randint(300, 8800)
    mountain = Mountain.objects.create(name=name, height=height)
    return name, height, mountain.pk


@pytest.fixture()
def sample_river():
    name, length = fake.word(), randint(300, 5000)
    river = River.objects.create(name=name, length=length)
    return name, length, river.pk
