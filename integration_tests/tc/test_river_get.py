import pytest
import requests

from .. import endpoints


class TestRiverGet:
    """Test for River"""

    def test_river_details(self, sample_river):
        """River Details"""
        expected_name, expected_length, expected_id = sample_river
        river_details_response = requests.get(endpoints.river_with_id(expected_id))
        assert river_details_response.status_code == 200
        actual_river = river_details_response.json()
        assert actual_river['name'] == expected_name
        assert actual_river['length'] == expected_length
