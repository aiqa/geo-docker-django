import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestMountainGet(BaseTest):
    """Test for Mountain: """

    @pytest.mark.django_db
    def test_mountain_details(self, client, sample_mountain):
        """Mountain Details"""
        expected_name, expected_height, expected_id = sample_mountain
        mountain_details_response = client.get(reverse('mountain-details', kwargs={'pk': expected_id}))
        assert mountain_details_response.status_code == 200
        actual_mountain = mountain_details_response.json()
        assert actual_mountain['name'] == expected_name
        assert actual_mountain['height'] == expected_height
