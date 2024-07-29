# tests/test_authentication.py
from .test_utils import MetricsTestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTests(MetricsTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_authentication_required(self):
        url = reverse('metric-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access(self):
        self.client.force_login(self.user)
        url = reverse('metric-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more authentication tests...