from django.db import models

class Employee(models.Model):
  name = models.CharField(max_length=100)
  department = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  # Add a field to store availability (can be a model field or JSON field)

class Shift(models.Model):
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  department = models.CharField(max_length=50)
  required_skills = models.CharField(max_length=255)
  # Consider adding a field for assigned employee (ForeignKey)
