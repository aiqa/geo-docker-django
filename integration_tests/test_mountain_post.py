import requests
from assertpy import assert_that

from . import endpoints
from .models import random_mountain_body


class TestMountainPost:
    """Test for Mountain: """

    def test_create_mountain(self):
        """Creating Mountain"""
        expected_mountain_body = random_mountain_body()
        mountain_creation_response = requests.post(endpoints.mountain_list, json=expected_mountain_body)
        assert mountain_creation_response.status_code == 201
        assert_that(mountain_creation_response.json()).is_equal_to(expected_mountain_body, include=['name', 'height'])
