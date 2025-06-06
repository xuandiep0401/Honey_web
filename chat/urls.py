from django.urls import path
from .views import chat_widget

urlpatterns = [
    path('', chat_widget, name='chat'),
]
