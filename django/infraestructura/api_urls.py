from rest_framework.routers import DefaultRouter
from .api_views import (
    NodoServidorViewSet,
    IncidenciaServidorViewSet,
    RegistroAuditoriaViewSet,
)

router = DefaultRouter()
router.register("nodos", NodoServidorViewSet)
router.register("incidencias", IncidenciaServidorViewSet)
router.register("auditoria", RegistroAuditoriaViewSet)

urlpatterns = router.urls