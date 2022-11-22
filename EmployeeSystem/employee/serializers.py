from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #All fields will be visible 
        fields = '__all__'

    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)