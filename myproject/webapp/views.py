from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import employees
from . serializers import employeeSerializer

class emplyeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializers=employeeSerializer(employees1,many=True)
        return Response(serializers.data)

    def post(self):
        pass
