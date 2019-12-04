import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestCityDelete(BaseTest):
    """Test for City: """

    @pytest.mark.django_db
    def test_delete_city(self, client, sample_city):
        """Deleting City"""
        _, _, city_id = sample_city
        city_delete_response = client.delete(reverse('city-details', kwargs={'pk': city_id}))
        assert city_delete_response.status_code == 204

        city_details_response = client.get(reverse('city-details', kwargs={'pk': city_id}))
        assert city_details_response.status_code == 404
