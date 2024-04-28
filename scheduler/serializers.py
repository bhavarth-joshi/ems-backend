from rest_framework import serializers
from .models import Employee, Shift

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'  # Include all fields for now (can be customized later)

class ShiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shift
    fields = '__all__'  # Include all fields for now (can be customized later)
