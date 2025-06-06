from django.test import Client
from django.urls import reverse

def test_landing_page(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
