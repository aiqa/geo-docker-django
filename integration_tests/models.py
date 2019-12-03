from random import randint

from faker import Faker

fake = Faker()


def random_city_body():
    return {
        'name': fake.city(),
        'population': randint(300, 5_000_000)
    }


def random_mountain_body():
    return {
        'name': fake.word(),
        'height': randint(300, 5000)
    }


def random_river_body():
    return {
        'name': fake.word(),
        'length': randint(300, 5000)
    }
