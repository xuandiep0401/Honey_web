from django.urls import path
from .views import my_points

urlpatterns = [
    path('', my_points, name='points'),
]
