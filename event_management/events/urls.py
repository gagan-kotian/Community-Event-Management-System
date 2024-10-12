# events/urls.py

from django.urls import path
from .views import register, user_login

urlpatterns = [
    path('register/', register, name='register'),  # URL for registration
    path('login/', user_login, name='login'),      # URL for login
]
