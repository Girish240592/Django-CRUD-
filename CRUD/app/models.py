from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    
    def __str__(self):
        return "Employees Data"
