from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employees
from .serializers import empserializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def employees(request):
    if request.method == 'GET':
        objemp = Employees.objects.all()
        serializer = empserializer(objemp, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data 
        serializer = empserializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = request.data 
        try:
            obj = Employees.objects.get(id=data['id'])
        except Employees.DoesNotExist:
            return Response({"ERROR": "Employee not found" }, status=404)
        
        serializer = empserializer(obj, data=data, partial=False)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = request.data 
        try:
            obj = Employees.objects.get(id=data['id'])
        except Employees.DoesNotExist:
            return Response({"ERROR": "Employee not found"}, status=404)

        serializer = empserializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data = request.data
        
    try:
        obj = Employees.objects.get(id=data['id'])
    except Employees.DoesNotExist:
        return Response({"error": "Employee not found"},status=404)
    
    obj.delete()
    return Response({"Message": "Employee deleted successfully"},status=204)



# class based

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import empserializer

class EmpView(APIView):
    def get(self, request):
        # Retrieve all Person objects
        emps = Employees.objects.all()
        serializer = empserializer(emps, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new Person object
        serializer = empserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Update an existing Person object
        try:
            emp = Employees.objects.get(id=request.data['id'])
        except emp.DoesNotExist:
            return Response({"ERROR": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = empserializer(emp, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        # Partially update an existing Person object
        try:
            emp = Employees.objects.get(id=request.data['id'])
        except emp.DoesNotExist:
            return Response({"ERROR": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = empserializer(emp, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Delete a Person object
        try:
            emp = Employees.objects.get(id=request.data['id'])
        except emp.DoesNotExist:
            return Response({"ERROR": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        emp.delete()
        return Response({"Message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


from rest_framework import viewsets
from .models import Employees
from .serializers import empserializer

class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()  # Define the queryset for the viewset
    serializer_class = empserializer  # Specify the serializer to be used
    
    
    
    
    
    
    
    
    
    
@api_view(['GET'])
def index(request):
    people_details = {
        "name": "Rithika",
        "age": 20,
        "designation": "Developer",
        "salary":10000
    }
    return Response(people_details)