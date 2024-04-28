from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Shift
from .serializers import EmployeeSerializer, ShiftSerializer


class EmployeeListCreateView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetailView(APIView):
    # Implement logic to retrieve a specific employee by ID
    # ...


class ShiftListCreateView(APIView):
    def get(self, request):
        shifts = Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ShiftDetailView(APIView):
    # Implement logic to retrieve a specific shift by ID
    # ...

# Similar views for assigning shifts and employee schedule retrieval can be added later
