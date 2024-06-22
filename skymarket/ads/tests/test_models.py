from django.contrib.auth import get_user_model
from django.test import TestCase
from ads.models import Ad, Comment

User = get_user_model()


class AdModelTest(TestCase):

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

    def test_ad_creation(self):
        self.assertEqual(self.ad.title, "Test Ad")
        self.assertEqual(self.ad.price, 100)
        self.assertEqual(self.ad.author, self.user)


class CommentModelTest(TestCase):

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
        self.comment = Comment.objects.create(text="Test Comment", author=self.user, ad=self.ad)

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, "Test Comment")
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.ad, self.ad)
