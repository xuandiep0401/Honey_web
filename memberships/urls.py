from django.urls import path
from .views import my_membership

urlpatterns = [
    path('', my_membership, name='membership'),
]
