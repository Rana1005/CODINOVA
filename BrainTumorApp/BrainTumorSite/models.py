from datetime import date
import email
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    imgcheck = models.CharField(max_length=100)
