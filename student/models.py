from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    course = models.CharField(max_length=100, null=True)