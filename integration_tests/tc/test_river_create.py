import pytest
import requests
from assertpy import assert_that

from .. import endpoints
from ..models import random_river_body


class TestRiverCreate:
    """Test for River"""

    def test_create_river(self):
        """Creating River"""
        expected_river_body = random_river_body()
        river_creation_response = requests.post(endpoints.river_list, json=expected_river_body)
        assert river_creation_response.status_code == 201
        assert_that(river_creation_response.json()).is_equal_to(expected_river_body, include=['name', 'length'])
