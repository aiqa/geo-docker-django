import pytest
from assertpy import assert_that
from django.urls import reverse

from .base_test import BaseTest


class TestCityPost(BaseTest):
    """Test for City: """

    @pytest.mark.django_db
    def test_create_city(self, client):
        """Creating City"""
        expected_city_body = self._random_city_body()
        city_creation_response = client.post(reverse('city-list'), expected_city_body)
        assert city_creation_response.status_code == 201
        assert_that(city_creation_response.json()).is_equal_to(expected_city_body, include=['name', 'population'])
