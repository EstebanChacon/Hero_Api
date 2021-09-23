from django.core.management.base import BaseCommand
from heroapi.models import heroapi
import csvfile

class command(BaseCommand):
    def handle(self, **options):
        print("Importing data ...") 
