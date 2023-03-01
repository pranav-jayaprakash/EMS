from rest_framework import serializers
from EmployeeApp.models import LeaveApplicationModel


class LeaveApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplicationModel
        exclude = ['employee','status']

    def create(self, validated_data):
        employee = self.context.get('employee')     
        return LeaveApplicationModel.objects.create(**validated_data, employee=employee)



class LeaveApplicationsListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = LeaveApplicationModel
        exclude = ['id', 'employee']

    def get(self, request,format=None):
        employee = request.user

        return LeaveApplicationModel.objects.filter(employee_id=employee.id)
         

