import pytest
from assertpy import assert_that
from django.urls import reverse

from .base_test import BaseTest


class TestRiverCreate(BaseTest):
    """Test for River"""

    @pytest.mark.django_db
    def test_create_river(self, client):
        """Creating River"""
        expected_river_body = self._random_river_body()
        river_creation_response = client.post(reverse('river-list'), expected_river_body)
        assert river_creation_response.status_code == 201
        assert_that(river_creation_response.json()).is_equal_to(expected_river_body, include=['name', 'length'])
