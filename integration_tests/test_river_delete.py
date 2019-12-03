import pytest
import requests

from . import endpoints


class TestRiverDelete:
    """Test for River"""

    def test_delete_river(self, sample_river):
        """Deleting River"""
        _, _, river_id = sample_river
        river_delete_response = requests.delete(endpoints.river_with_id(river_id))
        assert river_delete_response.status_code == 204

        river_details_response = requests.get(endpoints.river_with_id(river_id))
        assert river_details_response.status_code == 404
