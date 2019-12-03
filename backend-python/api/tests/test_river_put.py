import pytest
from assertpy import assert_that
from django.urls import reverse
from .base_test import BaseTest


class TestRiverPut(BaseTest):
    """Test for River"""

    @pytest.mark.django_db
    def test_update_river(self, client, sample_river):
        """Updating River"""
        _, _, river_id = sample_river
        new_river_body = self._random_river_body()
        river_update_response = client.put(reverse('river-details', kwargs={'pk': river_id}), new_river_body,
                                           content_type='application/json')
        assert river_update_response.status_code == 200

        river_details_response = client.get(reverse('river-details', kwargs={'pk': river_id}))
        actual_river = river_details_response.json()
        assert_that(actual_river).is_equal_to(new_river_body, include=['name', 'length'])
