from django.test import TestCase
import requests
from django import urls
from django.urls import reverse

class TestAPI(TestCase):
    def test_api(self, **kwargs):
        response = self.client.get('/router')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'city')