# metrics/urls_public.py
from django.urls import path, include
from django.conf import settings
from metrics import views
from metrics.admin import admin_site
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin and API token auth
    path('admin/', admin_site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # JWT token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Public URLs
    path('', views.public_home, name='home'),
    
    # API URLs
    path('api/', include('metrics.urls')),  # Include your API URLs here
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns