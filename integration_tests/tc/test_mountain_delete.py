import pytest
import requests

from .. import endpoints


class TestMountainDelete:
    """Test for Mountain: """

    def test_delete_mountain(self, sample_mountain):
        """Deleting Mountain"""
        _, _, mountain_id = sample_mountain
        mountain_delete_response = requests.delete(endpoints.mountain_with_id(mountain_id))
        assert mountain_delete_response.status_code == 204

        mountain_details_response = requests.get(endpoints.mountain_with_id(mountain_id))
        assert mountain_details_response.status_code == 404
