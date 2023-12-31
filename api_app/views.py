from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
import json 
from .models import *
from rest_framework import viewsets 
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serialize_class = CompanySerializer

    def get_serializer_class(self):
        return CompanySerializer
    
    @action(detail=True, methods = ['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many= True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exist !!'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serialize_class = EmployeeSerializer

    def get_serializer_class(self):
        return EmployeeSerializer