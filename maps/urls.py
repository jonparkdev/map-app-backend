from rest_framework import routers
from maps.api import LocationViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = router.urls
