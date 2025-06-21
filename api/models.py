# api/models.py
from djongo import models

# Modelo para coordenadas, que se usará como campo anidado
class Coordenadas(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        abstract = True # Importante: Esto evita que se cree una colección para Coordenadas

class PuntoReciclaje(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=255)
    tipo_material = models.JSONField() # Almacena la lista de materiales
    direccion = models.TextField()
    horario = models.CharField(max_length=255)
    coordenadas = models.EmbeddedField(
        model_container=Coordenadas
    )

    def __str__(self):
        return self.nombre

class CentroAcopio(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=255)
    tipo_residuo = models.JSONField()
    entidad = models.CharField(max_length=255)
    direccion = models.TextField()
    sitio_web = models.URLField(max_length=500, blank=True, null=True)
    coordenadas = models.EmbeddedField(
        model_container=Coordenadas
    )

    def __str__(self):
        return self.nombre

class MercadoOrganico(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    productos_destacados = models.JSONField()
    direccion = models.TextField()
    horario = models.CharField(max_length=255)
    coordenadas = models.EmbeddedField(
        model_container=Coordenadas
    )

    def __str__(self):
        return self.nombre

class PuntoRecargaElectrico(models.Model):
    _id = models.ObjectIdField()
    operador = models.CharField(max_length=255)
    tipo_conector = models.JSONField()
    potencia_kw = models.FloatField()
    direccion = models.TextField()
    costo = models.CharField(max_length=255)
    coordenadas = models.EmbeddedField(
        model_container=Coordenadas
    )

    def __str__(self):
        return self.operador + " - " + self.direccion

# Modelo para los puntos favoritos de un usuario
class PuntoFavorito(models.Model):
    id_punto = models.CharField(max_length=100)
    coleccion = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Usuario(models.Model):
    _id = models.ObjectIdField()
    nombre_usuario = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    hash_contrasena = models.CharField(max_length=255) # En un proyecto real, se usaría el sistema de auth de Django
    fecha_registro = models.DateTimeField()
    puntos_favoritos = models.ArrayField(
        model_container=PuntoFavorito
    )

    def __str__(self):
        return self.nombre_usuario