from unittest import TestCase
from rest_framework.authentication import get_user_model


class TestModel(TestCase):

    def create_user(self, email, password):
        return get_user_model().objects.create_user(
            email=email,
            password=password
    )

    def test_user_creation(self):
        email = "abheesh@example.com"
        password = "Password123"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_normalized_emails(self):
        emails = ["abheeshk@example.com", "abheeshK@EXAMPLE.com", "ABHEESHK@example.com", "abheeshk@exmaple.COM","abheeshk@ExAmPle.COM"]
        password = "Password123"

        for email in emails:
            user = self.create_user(email, password)
            self.assertEqual(user.email, email)
            self.assertEqual(user.check_password(password))