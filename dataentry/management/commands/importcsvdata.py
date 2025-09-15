from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

# command python manage.py importcsvdata file_path model_name

class Command(BaseCommand):
    help = "Import data from csv"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="path to the csv file")
        parser.add_argument('model_name', type=str, help="Name of the model")


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # search model name  
        model = None
        for app_config in apps.get_app_configs():
            try: 
                model = apps.get_model(app_config.label, model_name)
                break #stop search when model name found
            except LookupError:
                continue #continue search in next app 

        if not model:
            raise CommandError(f"Model {model_name} not found in any app")
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
                print(file)
        self.stdout.write(self.style.SUCCESS('Success data imported!'))