import pytest
from django.urls import reverse

def test_landing_page(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_page(client):
    url = reverse('account_login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Log in' in response.content.decode()
