# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PuntoReciclajeViewSet,
    CentroAcopioViewSet,
    MercadoOrganicoViewSet,
    PuntoRecargaElectricoViewSet,
    UsuarioViewSet
)

# Creamos un router que genera las URLs automáticamente
router = DefaultRouter()
router.register(r'puntos-reciclaje', PuntoReciclajeViewSet)
router.register(r'centros-acopio', CentroAcopioViewSet)
router.register(r'mercados-organicos', MercadoOrganicoViewSet)
router.register(r'puntos-recarga-electricos', PuntoRecargaElectricoViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]