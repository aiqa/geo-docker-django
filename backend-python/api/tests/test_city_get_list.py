import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestCityList(BaseTest):
    """Test for City: """

    @pytest.mark.django_db
    def test_city_list(self, client, sample_city):
        """City list"""
        city_list_response = client.get(reverse('city-list'))
        assert city_list_response.status_code == 200
        assert len(city_list_response.json()) > 0
