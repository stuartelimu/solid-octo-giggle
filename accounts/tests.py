from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def test_user(self):
        username = 'test'
        password = 'test@123'
        u = User(username=username)
        u.set_password(password)
        u.save()
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))