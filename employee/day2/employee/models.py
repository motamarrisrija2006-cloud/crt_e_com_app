from django.db import models

# Create your models here.

from django.db import models

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=20)
    designation = models.CharField(max_length=250)
    emp_type=models.CharField(max_length=250)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name