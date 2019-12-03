import pytest
import requests
from assertpy import assert_that

from . import endpoints
from .models import random_mountain_body


class TestMountainPut:
    """Test for Mountain: """

    def test_update_mountain(self, sample_mountain):
        """Updating Mountain"""
        _, _, mountain_id = sample_mountain
        new_mountain_body = random_mountain_body()
        mountain_update_response = requests.put(endpoints.mountain_with_id(mountain_id), json=new_mountain_body)
        assert mountain_update_response.status_code == 200

        mountain_details_response = requests.get(endpoints.mountain_with_id(mountain_id))
        actual_mountain = mountain_details_response.json()
        assert_that(actual_mountain).is_equal_to(new_mountain_body, include=['name', 'height'])
