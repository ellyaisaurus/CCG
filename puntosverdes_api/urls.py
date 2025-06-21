# puntosverdes_api/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import (
    portal_view,
    gestion_puntos_reciclaje,
    gestion_centros_acopio,
    gestion_mercados_organicos,
    gestion_puntos_recarga,
    gestion_usuarios,
)

urlpatterns = [
    # --- Rutas Principales y de Gestión ---
    path('', portal_view, name='portal'),
    path('admin/', admin.site.urls),

    # --- Rutas de Gestión Intuitivas ---
    path('gestion/puntos-reciclaje/', gestion_puntos_reciclaje, name='gestion_puntos_reciclaje'),
    path('gestion/centros-acopio/', gestion_centros_acopio, name='gestion_centros_acopio'),
    path('gestion/mercados-organicos/', gestion_mercados_organicos, name='gestion_mercados_organicos'),
    path('gestion/puntos-recarga/', gestion_puntos_recarga, name='gestion_puntos_recarga'),
    path('gestion/usuarios/', gestion_usuarios, name='gestion_usuarios'),

    # --- Rutas de la API (para desarrolladores) ---
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
