from django.conf.urls import url, include
from django.contrib import admin

from api import urls as api_urls
from dashboard import urls as dashboard_urls


urlpatterns = [
    # Django admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(api_urls, namespace='api')),

    # Dashboard views
    url(r'^', include(dashboard_urls, namespace='dashboard')),
]
