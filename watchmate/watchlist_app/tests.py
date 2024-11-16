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


class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamingPlatform.objects.create(name='Disney+', about="The world\'s largest streaming service", website="https://www.disneyplus.com/")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example", synopsis="Example synopsis", active=True)

    def test_watch_list_create(self):
        data = {
            'platform': self.stream,
            'title': 'The Shawshank Redemption',
            'synopsis': 'Two imprisoned men bond over a decade-long marriage.',
            'active': True,
        }
        response = self.client.post(reverse('watch_list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('watch_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_details(self):
        response = self.client.get(reverse('details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example')


# class ReviewTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='test123')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

#         data = {
#             'name': 'Disney+',
#             'about': 'The world\'s largest streaming service',
#             'website': 'https://www.disneyplus.com/'
#         }
#         self.stream = models.StreamingPlatform.objects.create(data)
#         self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example", synopsis="Example synopsis", active=True)
#         self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example 2", synopsis="Example synopsis 2", active=True)
#         self.review = models.Review.objects.create(review_user=self.user, rating=5, description="Great Moview",
#                                                    watchlist=self.watchlist2, active=True)

#     def test_review_create(self):
#         data = {
#             "review_user": self.user,
#             "rating": 5,
#             "description": self.watchlist,
#             "active": True,
#         }

#         response = self.client.post(reverse('review_create', args=(self.watchlist.id)), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(models.Review.objects.count(), 2)

#         response = self.client.post(reverse('review_create', args=(self.watchlist.id)), data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_review_create_unauth(self):
#         data = {
#             "review_user": self.user,
#             "rating": 5,
#             "description": self.watchlist,
#             "active": True,
#         }

#         self.client.force_authenticate(user=None)
#         response = self.client.post(reverse('review_create', args=(self.watchlist.id)), data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_review_update(self):
#         data = {
#             "review_user": self.user,
#             "rating": 4,
#             "description": self.watchlist,
#             "active": False,
#         }

#         response = self.client.put(reverse('review_detail', args=(self.review.id)), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_review_list(self):
#         response = self.client.get(reverse('review_list'), args=(self.watchlist.id, ))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_review_ind(self):
#         response = self.client.get(reverse('review_detail'), args=(self.review.id, ))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_review_user(self):
#         response = self.client.get('/watch/reviews/?username'+ self.user.username)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)