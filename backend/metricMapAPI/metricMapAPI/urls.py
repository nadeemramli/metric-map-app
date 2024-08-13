from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Metrics API",
      default_version='v1',
      description="API documentation for Mapping of Metrics",
      terms_of_service="https://www.nadeemramli.com/",
      contact=openapi.Contact(email="m.nadeemramli@gmail.com"),
      license=openapi.License(name="This project is licensed under the MIT License."),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger/OpenAPI routes
      path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Include public URLs
    path('', include('metricMapAPI.urls_public')),
]