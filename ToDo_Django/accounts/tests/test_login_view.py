from django.test import Client
from django.urls import reverse
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User.objects.create_superuser(username='test_user', password='AdfgS5784@')
    return user

@pytest.fixture
def url():
    url = reverse('accounts:login-view')
    return url

@pytest.mark.django_db
class TestLoginView:
    def test_get_response_200(self, client, url):
        response = client.get(url)
        assert response.status_code == 200
