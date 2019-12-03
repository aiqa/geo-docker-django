import requests
from assertpy import assert_that

from . import endpoints
from .models import random_city_body


class TestCityPost:
    """Test for City: """

    def test_create_city(self):
        """Creating City"""
        expected_city_body = random_city_body()
        city_creation_response = requests.post(endpoints.city_list, json=expected_city_body)
        assert city_creation_response.status_code == 201
        assert_that(city_creation_response.json()).is_equal_to(expected_city_body, include=['name', 'population'])
