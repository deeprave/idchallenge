from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
