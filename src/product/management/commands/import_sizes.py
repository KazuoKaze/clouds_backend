from django.core.management.base import BaseCommand
import pandas as pd

from product.models import ProductSize

from django.conf import settings
import os
from decouple import config



class Command(BaseCommand):
    help = 'Import product sizes from an Excel file'

    def handle(self, *args, **kwargs):
        file_name = config('FILE_NAME', cast=str)
        file_path = os.path.join(settings.BASE_DIR, file_name)

        try:
            data = pd.read_excel(file_path)
            row_name = config('NAME', cast=str)

            for index, row in data.iterrows():
                name = row[row_name]
                
                size, created = ProductSize.objects.get_or_create(name=name)
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added new size: {name}"))
                else:
                    self.stdout.write(f"Size {name} already exists")
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
