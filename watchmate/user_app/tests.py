from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
        }

        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username='testuser')
        self.assertTrue(Token.objects.filter(user=user).exists())