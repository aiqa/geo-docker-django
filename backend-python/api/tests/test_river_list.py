import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestRiverList(BaseTest):
    """Test for River"""

    @pytest.mark.django_db
    def test_river_list(self, client, sample_river):
        """River List"""
        river_list_response = client.get(reverse('river-list'))
        assert river_list_response.status_code == 200
        assert len(river_list_response.json()) > 0
