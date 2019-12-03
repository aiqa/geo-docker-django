import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestRiverDelete(BaseTest):
    """Test for River"""

    @pytest.mark.django_db
    def test_delete_river(self, client, sample_river):
        """Deleting River"""
        _, _, river_id = sample_river
        river_delete_response = client.delete(reverse('river-details', kwargs={'pk': river_id}))
        assert river_delete_response.status_code == 204

        river_details_response = client.get(reverse('river-details', kwargs={'pk': river_id}))
        assert river_details_response.status_code == 404
