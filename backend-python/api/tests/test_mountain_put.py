import pytest
from assertpy import assert_that
from django.urls import reverse

from .base_test import BaseTest


class TestMountainPut(BaseTest):
    """Test for Mountain: """

    @pytest.mark.django_db
    def test_update_mountain(self, client, sample_mountain):
        """Updating Mountain"""
        _, _, mountain_id = sample_mountain
        new_mountain_body = self._random_mountain_body()
        mountain_update_response = client.put(reverse('mountain-details', kwargs={'pk': mountain_id}),
                                              new_mountain_body, content_type='application/json')
        assert mountain_update_response.status_code == 200

        mountain_details_response = client.get(reverse('mountain-details', kwargs={'pk': mountain_id}))
        actual_mountain = mountain_details_response.json()
        assert_that(actual_mountain).is_equal_to(new_mountain_body, include=['name', 'height'])
