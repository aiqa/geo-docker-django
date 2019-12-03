import pytest
from django.urls import reverse

from .base_test import BaseTest


class TestMountainList(BaseTest):
    """Test for Mountain: """

    @pytest.mark.django_db
    def test_mountain_list(self, client, sample_mountain):
        """Mountain List"""
        mountain_list_response = client.get(reverse('mountain-list'))
        assert mountain_list_response.status_code == 200
        assert len(mountain_list_response.json()) > 0
