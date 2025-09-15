from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "Populate data to the database"

    def handle(self, *args, **kwargs):
        dataset = [
            {'matric_no': 1001, 'name':"Ann", 'age':21},
            {'matric_no': 1002, 'name':"Mike", 'age':19},
            {'matric_no': 1003, 'name':"John", 'age':18},
            {'matric_no': 1004, 'name':"Ike", 'age':20},
            {'matric_no': 1006, 'name':"Me", 'age':17},
        ]

        for data in dataset:
            matric_no=data['matric_no']
            existing_record = Student.objects.filter(matric_no=data['matric_no']).exists()

            if not existing_record:
                students = Student.objects.create(matric_no=data['matric_no'], name=data['name'], age=data['age'])
                self.stdout.write(self.style.SUCCESS(f"Data Matric No:{students.matric_no} name:{students.name} age:{students.age} inserted successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Student with matric no {matric_no} already exits"))