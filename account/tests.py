from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class AccountTests(APITestCase):

    def setUp(self):
        self.user_test_data = {
            'first_name': 'Osayi',
            'last_name': 'Akoko',
            'email': 'test@email.com',
            'password': 'password123',
        }
        User.objects.create_user(**self.user_test_data)

        return super().setUp()

    def _get_tokens(self):
        url = reverse('account:v1:login')
        response = self.client.post(url, self.user_test_data)
        access_token = response.data['access_token']
        refresh_token = response.data['refresh_token']

        return access_token, refresh_token

    def test_create_user(self):
        """
            Ensures user creation works properly, 
            by checking no of users in db after setUp exec.
        """
        users_count = User.objects.count()
        self.assertEqual(users_count, 1)

    def test_login(self):
        """
            Ensures dashboard user can login
        """

        url = reverse('account:v1:login')

        response = self.client.post(url, self.user_test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password(self):
        """
            Ensures dasboard users can change password
        """
        url = reverse('account:v1:change-password')
        access_token, _ = self._get_tokens()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        data = {
            'current_password': self.user_test_data['password'],
            'new_password': 'password123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token(self):
        """
            Ensures token can be refreshed
        """
        url = reverse('account:v1:refresh-token')
        
        _, refresh_token = self._get_tokens()
        data = { 'refresh_token': refresh_token, }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
