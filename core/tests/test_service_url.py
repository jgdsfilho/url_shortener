from core.models import User, Url
from django.test.testcases import TestCase
from core.tests import fixtures
from core.service.url_service import list_urls, add_url, get_url
import json


class TestServiceUrl(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()
        fixtures.short_url()

    def test_get_url_from_a_user(self):
        user = User.objects.all().first()
        urls_expected = [
            url.to_dict_json() for url in Url.objects.filter(logged_user=user)
        ]
        urls_expected = {'urls': urls_expected}
        urls = list_urls(user)
        self.assertEqual(urls_expected, urls)

    def test_create_url_to_a_user(self):
        user = User.objects.all().first()
        url = add_url("buser.com.br", user.id)
        url_expected = Url.objects.get(
            logged_user=user, url="buser.com.br"
        ).to_dict_json()
        self.assertEqual(url_expected, url)

    def test_get_specific_url(self):
        expected_url = Url.objects.all().first().to_dict_json()
        url = get_url(expected_url["short_url"])
        self.assertEqual(expected_url, url)

    def test_get_specific_url_not_found(self):
        url = get_url("543trew")
        self.assertEqual(False, url)
