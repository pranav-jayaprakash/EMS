from django.shortcuts import render
from EmployeeApp.models import LeaveApplicationModel
from rest_framework  import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import LeaveApplicationCreateSerializer, LeaveApplicationsListSerializer



class LeaveCreate(generics.CreateAPIView):
    queryset = LeaveApplicationModel.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LeaveApplicationCreateSerializer


    def create(self, request, *args, **kwargs):
        

        employee = request.user
        print(employee.id)


        if employee.is_superuser == 0:


            serializer = LeaveApplicationCreateSerializer(data = request.data, context={'employee': employee})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data= serializer.errors)
        

        else:
            return Response({'message':'Only Employee can access this Page'})


class LeaveList(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]  

    def get(self, request, format=None):
        employee = request.user


        filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
        search_fields = ['status']
        filterset_fields = ['apply_date','number_of_days']

        ordering_fields = ['apply_date','number_of_days']

        queryset = LeaveApplicationModel.objects.filter(employee_id=employee.id)
        serializer_class = LeaveApplicationsListSerializer(queryset, many=True)

        return Response(data=serializer_class.data)

class LeaveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveApplicationModel.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    serializer_class = LeaveApplicationCreateSerializer
