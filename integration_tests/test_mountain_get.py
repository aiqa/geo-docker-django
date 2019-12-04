import pytest
import requests

from . import endpoints


class TestMountainGet:
    """Test for Mountain: """

    def test_mountain_details(self, sample_mountain):
        """Mountain Details"""
        expected_name, expected_height, expected_id = sample_mountain
        mountain_details_response = requests.get(endpoints.mountain_with_id(expected_id))
        assert mountain_details_response.status_code == 200
        actual_mountain = mountain_details_response.json()
        assert actual_mountain['name'] == expected_name
        assert actual_mountain['height'] == expected_height
