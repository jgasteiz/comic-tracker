from rest_framework.routers import DefaultRouter

from api import views as api_views


router = DefaultRouter()
router.register(r'comics', api_views.Comics, base_name='comics')
router.register(r'new-releases', api_views.NewReleases, base_name='new-releases')
router.register(r'tracked-comics', api_views.TrackedComics, base_name='tracked-comics')
router.register(r'users', api_views.Users, base_name='users')
urlpatterns = router.urls
