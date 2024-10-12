# event_management/urls.py

from django.contrib import admin
from django.urls import path, include
from events.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home view for the root URL
    path('events/', include('events.urls')),  # Include events app URLs
]
