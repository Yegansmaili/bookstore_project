from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTest(TestCase):
    username = 'newusertest'
    email = 'newusertest@gmail.com'
    password = 'newusertest@y'

    def test_signup_url(self):
        res = self.client.get('/accounts/signup/')
        self.assertEqual(res.status_code, 200)

    def test_signup_url_by_name(self):
        res = self.client.get(reverse('signup'))
        self.assertEqual(res.status_code, 200)

    def test_signup_form(self):
        # custom_user = get_user_model()
        get_user_model().objects.create_user(
            self.username,
            self.email,
            self.password,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
