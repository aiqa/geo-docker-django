import pytest
import requests
from assertpy import assert_that

from . import endpoints
from .models import random_river_body


class TestRiverPut:
    """Test for River"""

    def test_update_river(self, sample_river):
        """Updating River"""
        _, _, river_id = sample_river
        new_river_body = random_river_body()
        river_update_response = requests.put(endpoints.river_with_id(river_id), json=new_river_body)
        assert river_update_response.status_code == 200

        river_details_response = requests.get(endpoints.river_with_id(river_id))
        actual_river = river_details_response.json()
        assert_that(actual_river).is_equal_to(new_river_body, include=['name', 'length'])
