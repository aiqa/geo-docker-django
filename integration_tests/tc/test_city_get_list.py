import pytest
import requests

from .. import endpoints


class TestCityList():
    """Test for City: """

    def test_city_list(self, sample_city):
        """City list"""
        city_list_response = requests.get(endpoints.city_list)
        assert city_list_response.status_code == 200
        assert len(city_list_response.json()) > 0
