from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv

# command python manage.py importcsvdata file_path

class Command(BaseCommand):
    help = "Import data from csv"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="path to the csv file")


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.create(**row)
                print(file)
        self.stdout.write(self.style.SUCCESS('Success data imported!'))