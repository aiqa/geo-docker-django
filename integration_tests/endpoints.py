import os

base_uri = f"{os.getenv('HOST')}/api" if os.getenv('HOST') else 'http://localhost:8000/api'
city_list = f'{base_uri}/city'
river_list = f'{base_uri}/river'
mountain_list = f'{base_uri}/mountain'


def city_with_id(city_id):
    return f'{city_list}/{city_id}'


def river_with_id(river_id):
    return f'{river_list}/{river_id}'


def mountain_with_id(mountain_id):
    return f'{mountain_list}/{mountain_id}'
