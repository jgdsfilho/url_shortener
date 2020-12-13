from core.models import Url, User
from hashlib import blake2b


def generate_short_url(url):
    return blake2b(url.encode("utf-8"), digest_size=4).hexdigest()


def add_url(url, user):
    short_url = generate_short_url(url)
    user_object = User.objects.get(id=user)
    url = Url.objects.get_or_create(
        url=url, short_url=short_url, logged_user=user_object
    )
    return url[0].to_dict_json()


def list_urls(user):
    urls = Url.objects.filter(logged_user=user)
    return [url.to_dict_json() for url in urls]


def get_url(short_url):
    url = Url.objects.filter(short_url=short_url)
    if url:
        return url[0].to_dict_json()
    return False
