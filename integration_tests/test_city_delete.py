import pytest
import requests

from . import endpoints


class TestCityDelete():
    """Test for City: """

    def test_delete_city(self, sample_city):
        """Deleting City"""
        _, _, city_id = sample_city
        city_delete_response = requests.delete(endpoints.city_with_id(city_id))
        assert city_delete_response.status_code == 204

        city_details_response = requests.get(endpoints.city_with_id(city_id))
        assert city_details_response.status_code == 404
