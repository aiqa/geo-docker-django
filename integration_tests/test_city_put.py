import pytest
import requests
from assertpy import assert_that

from . import endpoints
from .models import random_city_body


class TestCityPut():
    """Test for City: """

    def test_update_city(self, sample_city):
        """Updating City"""
        _, _, city_id = sample_city
        new_city_body = random_city_body()
        city_update_response = requests.put(endpoints.city_with_id(city_id), json=new_city_body)
        assert city_update_response.status_code == 200

        city_details_response = requests.get(endpoints.city_with_id(city_id))
        actual_city = city_details_response.json()
        assert_that(actual_city).is_equal_to(new_city_body, include=['name', 'population'])
