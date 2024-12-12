from django.test import TestCase
from rest_framework.authentication import get_user_model

def create_user(email="abhesh@example.com", password="password123"):
    return get_user_model().objects.create_user(
        email=email,
        password=password
    )

class ModelTests(TestCase):
    def test_user_creation(self):
        email = "abheesh@example.com"
        password = "Password123"

        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_normalized_emails(self):
        emails = ["abheeshk@example.com", "abheeshk@EXAMPLE.com", "abheeshk@example.COM","abheeshk@ExAmPle.COM"]
        password = "Password123"
        correct_email = "abheeshk@example.com"

        for email in emails:
            user = create_user(email, password)
            self.assertEqual(user.email, correct_email)
            self.assertTrue(user.check_password(password))
            user.delete()

    def test_empty_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='password123'
            )

    def test_superuser_creation(self):
        user = get_user_model().objects.create_superuser(
            email="abhesh@example.com",
            password="password123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)