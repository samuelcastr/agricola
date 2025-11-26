from rest_framework.routers import DefaultRouter
from .views import CosechaViewSet

router = DefaultRouter()
router.register(r'cosechas', CosechaViewSet, basename='cosechas')

urlpatterns = router.urls



