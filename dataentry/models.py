from django.db import models

# Create your models here.
class Student(models.Model):
    matric_no = models.CharField(max_length=100) 
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name