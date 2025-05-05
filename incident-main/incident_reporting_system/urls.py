# incident_reporting_system/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('incident_manager.urls')),  # Include your app's URLs here
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    # Add other URL configurations as needed
]
