from rest_framework import routers
from .api import MessageViewSet

router = routers.DefaultRouter()
router.register('api/basicapp', MessageViewSet, 'basicapp-api')

urlpatterns = router.urls