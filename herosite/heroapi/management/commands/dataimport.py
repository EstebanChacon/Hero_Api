from django.core.management.base import BaseCommand
from heroapi.models import Hero, Publisher

import csv

class Command(BaseCommand):
    def handle(self, **options):
        print("Importing data ...")
        CSV_FILE = '../superhero_dataset_full/superheroes_test_dataset.csv'
        with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
            herolist = [{k: v for k, v in row.items()}
                        for row in csv.DictReader(csvfile, skipinitialspace=True)]

            for item in herolist:
                publisher_params = {
                    "name": item['creator']
                }

                publisher = Publisher(**publisher_params)
                publisher.save()
                print(f"{publisher.name} created ...")

                hero_params = {
                    "name": item['name'],
                    "alias": item['real_name'],
                    "publisher": publisher_params["name"]
                }

                hero = Hero(**hero_params)
                hero.save()
                print(f"{hero.name} created ...")
