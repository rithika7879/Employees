from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    
    
def __str__(self):
        return self.name