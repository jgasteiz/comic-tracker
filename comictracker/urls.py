from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

from api import urls as api_urls
from dashboard import urls as dashboard_urls


urlpatterns = [
    # Django admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(api_urls, namespace='api')),
    url(r'^api-token-auth/', obtain_auth_token),

    # Dashboard views
    url(r'^', include(dashboard_urls, namespace='dashboard')),
]
