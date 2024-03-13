from django.test import TestCase
from django.urls import reverse


class HomepageTest(TestCase):
    def test_home_page_url(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_home_page_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_home_page_content(self):
        res = self.client.get(reverse('home'))
        self.assertContains(res, 'Home page')

    def test_home_page_template_used(self):
        res = self.client.get(reverse('home'))
        self.assertTemplateUsed(res, 'home.html')
