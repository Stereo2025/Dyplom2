from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from ads.models import Ad

User = get_user_model()


class AdViewSetTest(APITestCase):

    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            phone="1234567890"
        )
        self.ad = Ad.objects.create(title="Test Ad", price=100, author=self.user)
        self.url = reverse('ad-list')

        # Аутентификация с использованием JWT токена
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_list_ads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ad(self):
        data = {"title": "New Ad", "price": 200}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentViewSetTest(APITestCase):

    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            phone="1234567890"
        )
        self.ad = Ad.objects.create(title="Test Ad", price=100, author=self.user)

        # URL для создания комментария
        self.comment_create_url = f"/api/ads/{self.ad.id}/comments/"

        # Аутентификация с использованием JWT токена
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_list_comments(self):
        response = self.client.get(self.comment_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        data = {"text": "New Comment"}
        response = self.client.post(self.comment_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

