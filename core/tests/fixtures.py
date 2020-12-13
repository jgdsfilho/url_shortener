from core.models import User, Url
from hashlib import blake2b

def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze

def another_user():
    outro = User.objects.create_user(
        username='teste',
        first_name='Teste',
        last_name='Snow2',
        email='teste@example.com',
        password='1234',
    )
    return outro


def short_url():
    user = User.objects.all().first()
    url = Url.objects.create(
        url = 'google.com',
        short_url = blake2b(digest_size=4).hexdigest(),
        logged_user = user
    )
    return url