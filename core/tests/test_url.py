from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestAuthApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()
        fixtures.short_url()

    def test_list_url_from_a_user(self):
        client = Client()
        client.force_login(User.objects.get(username='jon'))
        r1 = client.get('/api/url')
        self.assertEqual({200}, {r.status_code for r in [r1]})

    def test_creat_new_short_url(self):
        client = Client()
        client.force_login(User.objects.get(username='jon'))
        r1 = client.post('/api/url', {'url': 'https://www.buser.com.br/'})
        self.assertEqual(201, r1.status_code)

