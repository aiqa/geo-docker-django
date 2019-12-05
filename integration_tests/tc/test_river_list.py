import pytest
import requests

from .. import endpoints


class TestRiverList:
    """Test for River"""

    def test_river_list(self, sample_river):
        """River List"""
        river_list_response = requests.get(endpoints.river_list)
        assert river_list_response.status_code == 200
        assert len(river_list_response.json()) > 0
