import pytest
from assertpy import assert_that
from django.urls import reverse

from .base_test import BaseTest


class TestCityPut(BaseTest):
    """Test for City: """

    @pytest.mark.django_db
    def test_update_city(self, client, sample_city):
        """Updating City"""
        _, _, city_id = sample_city
        new_city_body = self._random_city_body()
        city_update_response = client.put(reverse('city-details', kwargs={'pk': city_id}), new_city_body,
                                          content_type='application/json')
        assert city_update_response.status_code == 200

        city_details_response = client.get(reverse('city-details', kwargs={'pk': city_id}))
        actual_city = city_details_response.json()
        assert_that(actual_city).is_equal_to(new_city_body, include=['name', 'population'])
