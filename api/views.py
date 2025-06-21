# api/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets

# Importar Modelos
from .models import (
    PuntoReciclaje,
    CentroAcopio,
    MercadoOrganico,
    PuntoRecargaElectrico,
    Usuario
)
# Importar Serializers (para la API)
from .serializers import (
    PuntoReciclajeSerializer,
    CentroAcopioSerializer,
    MercadoOrganicoSerializer,
    PuntoRecargaElectricoSerializer,
    UsuarioSerializer
)
# Importar Forms (para las vistas de gestión)
from .forms import (
    PuntoReciclajeForm,
    CentroAcopioForm,
    MercadoOrganicoForm,
    PuntoRecargaElectricoForm,
    UsuarioForm
)

# --- Vistas para la API RESTful (El "motor" de la API) ---
# (Estas no cambian)
class PuntoReciclajeViewSet(viewsets.ModelViewSet):
    queryset = PuntoReciclaje.objects.all()
    serializer_class = PuntoReciclajeSerializer
# ... (las otras ViewSets siguen aquí igual) ...
class CentroAcopioViewSet(viewsets.ModelViewSet):
    queryset = CentroAcopio.objects.all()
    serializer_class = CentroAcopioSerializer
class MercadoOrganicoViewSet(viewsets.ModelViewSet):
    queryset = MercadoOrganico.objects.all()
    serializer_class = MercadoOrganicoSerializer
class PuntoRecargaElectricoViewSet(viewsets.ModelViewSet):
    queryset = PuntoRecargaElectrico.objects.all()
    serializer_class = PuntoRecargaElectricoSerializer
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# --- Vistas para el Portal y las Interfaces de Gestión Intuitivas ---

def portal_view(request):
    """Renderiza la página de inicio del portal (index.html)."""
    return render(request, 'index.html')

# --- Vistas de Gestión CRUD para cada modelo (CORREGIDAS) ---

def gestion_puntos_reciclaje(request):
    if request.method == 'POST':
        form = PuntoReciclajeForm(request.POST) # Usa el Form
        if form.is_valid():
            form.save()
            messages.success(request, '¡Punto de reciclaje añadido con éxito!')
        else:
            messages.error(request, 'Error al añadir el punto. Revisa los datos.')
        return redirect('gestion_puntos_reciclaje')
    
    context = {
        'items': PuntoReciclaje.objects.all().order_by('-_id'),
        'form': PuntoReciclajeForm() # Pasa una instancia del Form
    }
    return render(request, 'gestion/puntos_reciclaje_gestion.html', context)


def gestion_centros_acopio(request):
    if request.method == 'POST':
        form = CentroAcopioForm(request.POST) # Usa el Form
        if form.is_valid():
            form.save()
            messages.success(request, '¡Centro de acopio añadido con éxito!')
        else:
            messages.error(request, 'Error al añadir el centro. Revisa los datos.')
        return redirect('gestion_centros_acopio')

    context = {
        'items': CentroAcopio.objects.all().order_by('-_id'),
        'form': CentroAcopioForm() # Pasa una instancia del Form
    }
    return render(request, 'gestion/centros_acopio_gestion.html', context)


def gestion_mercados_organicos(request):
    if request.method == 'POST':
        form = MercadoOrganicoForm(request.POST) # Usa el Form
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mercado orgánico añadido con éxito!')
        else:
            messages.error(request, 'Error al añadir el mercado. Revisa los datos.')
        return redirect('gestion_mercados_organicos')
        
    context = {
        'items': MercadoOrganico.objects.all().order_by('-_id'),
        'form': MercadoOrganicoForm() # Pasa una instancia del Form
    }
    return render(request, 'gestion/mercados_organicos_gestion.html', context)


def gestion_puntos_recarga(request):
    if request.method == 'POST':
        form = PuntoRecargaElectricoForm(request.POST) # Usa el Form
        if form.is_valid():
            form.save()
            messages.success(request, '¡Punto de recarga añadido con éxito!')
        else:
            messages.error(request, 'Error al añadir el punto. Revisa los datos.')
        return redirect('gestion_puntos_recarga')

    context = {
        'items': PuntoRecargaElectrico.objects.all().order_by('-_id'),
        'form': PuntoRecargaElectricoForm() # Pasa una instancia del Form
    }
    return render(request, 'gestion/puntos_recarga_electricos_gestion.html', context)


def gestion_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) # Usa el Form
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario añadido con éxito!')
        else:
            messages.error(request, 'Error al añadir el usuario. Revisa los datos.')
        return redirect('gestion_usuarios')

    context = {
        'items': Usuario.objects.all().order_by('-_id'),
        'form': UsuarioForm() # Pasa una instancia del Form
    }
    return render(request, 'gestion/usuarios_gestion.html', context)