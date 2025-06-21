# api/forms.py
import json
from django import forms
from .models import (
    PuntoReciclaje, CentroAcopio, MercadoOrganico,
    PuntoRecargaElectrico, Usuario
)

# --- Base Form for Styling ---
class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field, forms.JSONField):
                placeholder_text = "Ingrese valores separados por comas. Ej: PET, Vidrio"
                if name == 'puntos_favoritos':
                    placeholder_text = 'Ingrese datos en formato JSON. Ej: [{"id_punto": "...", "coleccion": "..."}]'
                field.widget = forms.Textarea(attrs={
                    'class': 'form-control', 'rows': 3, 'placeholder': placeholder_text
                })

# --- Mixin para manejar Coordenadas ---
class CoordenadasFormMixin(forms.Form):
    """
    Un Mixin que añade campos explícitos para latitud y longitud,
    haciendo el manejo de coordenadas más robusto.
    """
    latitud = forms.FloatField(label="Latitud de Coordenadas", required=True)
    longitud = forms.FloatField(label="Longitud de Coordenadas", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitud'].widget.attrs.update({'class': 'form-control', 'step': 'any'})
        self.fields['longitud'].widget.attrs.update({'class': 'form-control', 'step': 'any'})

# --- Formularios Inteligentes para cada Modelo ---

class PuntoReciclajeForm(StyledModelForm, CoordenadasFormMixin):
    class Meta:
        model = PuntoReciclaje
        exclude = ['_id', 'coordenadas'] # Excluimos el campo original

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordenadas = {
            'lat': self.cleaned_data.get('latitud'),
            'lng': self.cleaned_data.get('longitud')
        }
        if commit:
            instance.save()
        return instance

    def clean_tipo_material(self):
        data = self.cleaned_data['tipo_material']
        if isinstance(data, str):
            return [item.strip() for item in data.split(',') if item.strip()]
        return data

class CentroAcopioForm(StyledModelForm, CoordenadasFormMixin):
    class Meta:
        model = CentroAcopio
        exclude = ['_id', 'coordenadas']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordenadas = {
            'lat': self.cleaned_data.get('latitud'),
            'lng': self.cleaned_data.get('longitud')
        }
        if commit:
            instance.save()
        return instance
    
    def clean_tipo_residuo(self):
        data = self.cleaned_data['tipo_residuo']
        if isinstance(data, str):
            return [item.strip() for item in data.split(',') if item.strip()]
        return data

class MercadoOrganicoForm(StyledModelForm, CoordenadasFormMixin):
    class Meta:
        model = MercadoOrganico
        exclude = ['_id', 'coordenadas']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordenadas = {
            'lat': self.cleaned_data.get('latitud'),
            'lng': self.cleaned_data.get('longitud')
        }
        if commit:
            instance.save()
        return instance

    def clean_productos_destacados(self):
        data = self.cleaned_data['productos_destacados']
        if isinstance(data, str):
            return [item.strip() for item in data.split(',') if item.strip()]
        return data

class PuntoRecargaElectricoForm(StyledModelForm, CoordenadasFormMixin):
    class Meta:
        model = PuntoRecargaElectrico
        exclude = ['_id', 'coordenadas']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordenadas = {
            'lat': self.cleaned_data.get('latitud'),
            'lng': self.cleaned_data.get('longitud')
        }
        if commit:
            instance.save()
        return instance

    def clean_tipo_conector(self):
        data = self.cleaned_data['tipo_conector']
        if isinstance(data, str):
            return [item.strip() for item in data.split(',') if item.strip()]
        return data

# El formulario de Usuario no tiene coordenadas, por lo que es más simple.
class UsuarioForm(StyledModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    def clean_puntos_favoritos(self):
        data = self.cleaned_data['puntos_favoritos']
        if isinstance(data, str):
            try:
                if not data.strip(): return []
                return json.loads(data)
            except json.JSONDecodeError:
                raise forms.ValidationError("El formato JSON para Puntos Favoritos es inválido.")
        return data
