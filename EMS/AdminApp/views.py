from django.shortcuts import render
from AdminApp.models import EmployeeModel
from EmployeeApp.models import LeaveApplicationModel
from rest_framework  import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EmployeeCreateSerializer,EmployeeListSerializer, LeaveApplicationListSerializer, LeaveApplicationUpdateSerializer


class EmployeeCreate(generics.CreateAPIView):
    queryset = EmployeeModel.objects.all()
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = EmployeeCreateSerializer


class EmployeeList(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = EmployeeListSerializer
    
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['id', 'employee_name', 'work_location']
    
    ordering_fields = ['id', 'employee_name', 'work_location']
    


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    
    serializer_class = EmployeeCreateSerializer


class LeaveApplicationList(generics.ListAPIView):
    queryset = LeaveApplicationModel.objects.all()
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = LeaveApplicationListSerializer
    
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['status']
    
    ordering_fields = ['employee', 'status',]
   


class LeaveApplicationUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveApplicationModel.objects.all()
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = LeaveApplicationUpdateSerializer
