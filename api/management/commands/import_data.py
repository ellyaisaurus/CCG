# api/management/commands/import_data.py
import json
from django.core.management.base import BaseCommand
from api.models import PuntoReciclaje, CentroAcopio, MercadoOrganico, PuntoRecargaElectrico, Usuario
from pathlib import Path

class Command(BaseCommand):
    help = 'Importa datos desde archivos JSON a la base de datos MongoDB'

    def handle(self, *args, **kwargs):
        base_path = Path(__file__).resolve().parent.parent.parent / 'data'

        # Limpiar colecciones antes de importar
        self.stdout.write('Limpiando colecciones existentes...')
        PuntoReciclaje.objects.all().delete()
        CentroAcopio.objects.all().delete()
        MercadoOrganico.objects.all().delete()
        PuntoRecargaElectrico.objects.all().delete()
        Usuario.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Colecciones limpiadas.'))

        # Diccionario para mapear archivos a modelos
        files_to_models = {
            'CCG_Centros_de_acopio.puntos_reciclaje.json': PuntoReciclaje,
            'CCG_Centros_de_acopio.centros_acopio.json': CentroAcopio,
            'CCG_Centros_de_acopio.mercados_organicos.json': MercadoOrganico,
            'CCG_Centros_de_acopio.puntos_recarga_electricos.json': PuntoRecargaElectrico,
            'CCG_Centros_de_acopio.usuarios.json': Usuario,
        }

        for file_name, model in files_to_models.items():
            file_path = base_path / file_name
            self.stdout.write(f'Importando datos desde {file_name}...')

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                for item in data:
                    # Eliminar el _id original para que MongoDB genere uno nuevo
                    if '_id' in item:
                        del item['_id']

                    # Crear la instancia del modelo y guardarla
                    try:
                        model.objects.create(**item)
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error al importar item de {file_name}: {item}\nError: {e}'))

            self.stdout.write(self.style.SUCCESS(f'Datos de {file_name} importados correctamente.'))

        self.stdout.write(self.style.SUCCESS('¡Todos los datos han sido importados!'))
