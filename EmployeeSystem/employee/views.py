from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    # get all Employees
    queryset = Employee.objects.all()
    #serialising the output
    serializer_class = EmployeeSerializer
    # authentication is required to perform any operation
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]






# class EmployeeView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         #many tells serializer that more than one objects needs to serialize
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response({"employees": serializer.data})

    # def post(self, request):
    #     employee = request.data.get('employee')

    #     # Create an article from the above data
    #     serializer = EmployeeSerializer(data=employee)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #     return Response({"success": "Employee  added successfully"})

