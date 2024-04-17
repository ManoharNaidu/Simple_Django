from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [("M","Male"), ("F","Female")]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DoB = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    address = models.CharField(max_length=100)
    department = models.ManyToManyField('Department')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Department(models.Model):
    department_name = models.CharField(max_length=50)