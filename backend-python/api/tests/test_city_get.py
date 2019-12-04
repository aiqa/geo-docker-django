import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestCityGet(BaseTest):
    """Test for City: """

    @pytest.mark.django_db
    def test_city_details(self, client, sample_city):
        """City Details"""
        expected_name, expected_population, expected_id = sample_city
        city_details_response = client.get(reverse('city-details', kwargs={'pk': expected_id}))
        assert city_details_response.status_code == 200
        actual_city = city_details_response.json()
        assert actual_city['name'] == expected_name
        assert actual_city['population'] == expected_population
