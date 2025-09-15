from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "Populate data to the database"

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': 1001, 'name':"Ann", 'age':21},
            {'roll_no': 1002, 'name':"Mike", 'age':19},
            {'roll_no': 1003, 'name':"John", 'age':18},
            {'roll_no': 1004, 'name':"Ike", 'age':20},
            {'roll_no': 1006, 'name':"Me", 'age':17},
        ]

        for data in dataset:
            roll_no=data['roll_no']
            existing_record = Student.objects.filter(roll_no=data['roll_no']).exists()

            if not existing_record:
                students = Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
                self.stdout.write(self.style.SUCCESS(f"Data Matric No:{students.roll_no} name:{students.name} age:{students.age} inserted successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Student with matric no {roll_no} already exits"))