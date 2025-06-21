# api/serializers.py
from rest_framework import serializers
from .models import (
    PuntoReciclaje,
    CentroAcopio,
    MercadoOrganico,
    PuntoRecargaElectrico,
    Usuario
)

class PuntoReciclajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoReciclaje
        fields = '__all__'

class CentroAcopioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroAcopio
        fields = '__all__'

class MercadoOrganicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MercadoOrganico
        fields = '__all__'

class PuntoRecargaElectricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoRecargaElectrico
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'