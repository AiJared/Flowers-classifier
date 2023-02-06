from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("classifier.urls", namespace="classifier")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # setting this to view media files from admin panel
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
