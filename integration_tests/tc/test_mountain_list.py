import pytest
import requests

from .. import endpoints


class TestMountainList:
    """Test for Mountain: """

    def test_mountain_list(self, sample_mountain):
        """Mountain List"""
        mountain_list_response = requests.get(endpoints.mountain_list)
        assert mountain_list_response.status_code == 200
        assert len(mountain_list_response.json()) > 0
