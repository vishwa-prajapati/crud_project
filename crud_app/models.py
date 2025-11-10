from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(unique=True, default='')
    age = models.IntegerField(default=0)
    salary = models.FloatField(default=0.0)
    address = models.TextField(default='')
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.name} - {self.email} - {self.age}- {self.salary} - {self.address}"