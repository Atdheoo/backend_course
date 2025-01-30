from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Backend Online Shop API",
        default_version='1.0.0',
        description="This is swagger for our apis."
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onlineshop.urls')),  # Includes your onlineshop URLs
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
