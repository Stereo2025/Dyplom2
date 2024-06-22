from django.contrib.auth import get_user_model
from django.test import TestCase
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer
from django.urls import reverse

User = get_user_model()


class AdSerializerTest(TestCase):
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
        self.serializer = AdSerializer(instance=self.ad)
        self.url = reverse('ad-list')

    def test_ad_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.ad.title)
        self.assertEqual(data['price'], self.ad.price)


class CommentSerializerTest(TestCase):

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
        # Создание комментария
        self.comment = Comment.objects.create(
            text="This is a test comment",
            author=self.user,
            ad=self.ad
        )
        self.serializer = CommentSerializer(instance=self.comment)
        self.url = reverse('ad-list')

    def test_comment_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['text'], self.comment.text)
        self.assertEqual(data['author_id'], self.comment.author.id)
        self.assertEqual(data['ad_id'], self.comment.ad.id)
