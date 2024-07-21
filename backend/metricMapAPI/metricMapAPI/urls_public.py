# metrics/urls_public.py
from django.urls import path, include
from django.conf import settings
from metrics import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Admin and API token auth
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # Include app-level URLs (this should include your clients endpoint)
    path('api/', include('metrics.urls')),  # Ensure this line is present and correct
    
    # Public URLs
    path('', views.public_home, name='home'),
 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns