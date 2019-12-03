import pytest
from assertpy import assert_that
from django.urls import reverse

from .base_test import BaseTest


class TestMountainPost(BaseTest):
    """Test for Mountain: """

    @pytest.mark.django_db
    def test_create_mountain(self, client):
        """Creating Mountain"""
        expected_mountain_body = self._random_mountain_body()
        mountain_creation_response = client.post(reverse('mountain-list'), expected_mountain_body)
        assert mountain_creation_response.status_code == 201
        assert_that(mountain_creation_response.json()).is_equal_to(expected_mountain_body, include=['name', 'height'])
