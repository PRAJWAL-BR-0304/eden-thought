from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URL patterns definition
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', include('journal.urls')),  # Include URLs from the journal app
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
