from django.core.management.base import BaseCommand
from heroapi.models import Hero

import csv

class Command(BaseCommand):
    def handle(self, **options):
        print("Importing data ...")
