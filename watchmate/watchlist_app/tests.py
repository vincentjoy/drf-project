from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from watchlist_app import serializers, models

class StreamingPlatformTestCase(APITestCase):

    # def setUp(self):
        # self.user = User.objects.create_user(username='testuser', password='test123')
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        # data = {
        #     'name': 'Disney+',
        #     'about': 'The world\'s largest streaming service',
        #     'website': 'https://www.disneyplus.com/'
        # }
        # self.stream = models.StreamingPlatform.objects.create(**data)

    def test_streaming_platform_create(self):
        data = {
            'name': 'Netflix',
            'about': 'The world\'s largest streaming service',
            'website': 'https://www.netflix.com/'
        }
        response = self.client.post(reverse('streaming_platform-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.StreamingPlatform.objects.count(), 1)
        self.assertEqual(models.StreamingPlatform.objects.get().name, 'Netflix')

    def test_streaming_platform_list(self):
        data = {
            'name': 'Hulu',
            'about': 'The largest entertainment company in the world',
            'website': 'https://www.hulu.com/'
        }
        self.client.post(reverse('streaming_platform-list'), data, format='json')
        response = self.client.get(reverse('streaming_platform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Hulu')

    def test_streaming_platform_detail(self):
        data = {
            'name': 'Amazon Prime Video',
            'about': 'The world\'s largest streaming service',
            'website': 'https://www.amazon.com/primevideo/'
        }
        response = self.client.post(reverse('streaming_platform-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
