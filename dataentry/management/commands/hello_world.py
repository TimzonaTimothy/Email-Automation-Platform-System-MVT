from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello world"


    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies name')

    def handle(self, *args, **kwargs):
        name = kwargs['name'] 
        self.stdout.write(self.style.SUCCESS(f"Hello {name}"))