import pytest
import requests

from . import endpoints


class TestCityGet:
    """Test for City: """

    def test_city_details(self, sample_city):
        """City Details"""
        expected_name, expected_population, expected_id = sample_city
        city_details_response = requests.get(endpoints.city_with_id(expected_id))
        assert city_details_response.status_code == 200
        actual_city = city_details_response.json()
        assert actual_city['name'] == expected_name
        assert actual_city['population'] == expected_population
