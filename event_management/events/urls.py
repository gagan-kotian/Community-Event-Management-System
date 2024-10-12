# events/urls.py

from django.urls import path
from .views import home, register, user_login,user_logout, add_event, event_list, edit_event, delete_event



urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_event, name='add_event'),
    path('list/', event_list, name='event_list'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),  # Add this line for editing events
    path('delete/<int:event_id>/', delete_event, name='delete_event'),  # Add this line for deleting events
]
