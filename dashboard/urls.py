from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^fetch-comics/$', login_required(views.fetch_comics), name='fetch_comics'),
    url(r'^login/$', views.login, name='login'),
    url(r'^$', login_required(views.home), name='home'),
]
