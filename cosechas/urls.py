from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CultivoViewSet, CosechaViewSet

router = DefaultRouter()
router.register("cultivos", CultivoViewSet)
router.register("cosechas", CosechaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


