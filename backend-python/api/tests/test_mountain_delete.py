import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestMountainDelete(BaseTest):
    """Test for Mountain: """

    @pytest.mark.django_db
    def test_delete_mountain(self, client, sample_mountain):
        """Deleting Mountain"""
        _, _, mountain_id = sample_mountain
        mountain_delete_response = client.delete(reverse('mountain-details', kwargs={'pk': mountain_id}))
        assert mountain_delete_response.status_code == 204

        mountain_details_response = client.get(reverse('mountain-details', kwargs={'pk': mountain_id}))
        assert mountain_details_response.status_code == 404
