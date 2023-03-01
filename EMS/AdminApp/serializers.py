
from rest_framework import serializers
from AdminApp.models import EmployeeModel
from EmployeeApp.models import LeaveApplicationModel
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class EmployeeCreateSerializer(serializers.ModelSerializer):


    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
    
    class Meta:
        model = EmployeeModel
        exclude = ['employee']

 
    def create(self, validated_data):


        employee = User(email=self.validated_data['email'], username=self.validated_data['email'])
        password =  self.validated_data['password']
        

        employee.set_password(password)
        

        employee.save()
        
 
        return EmployeeModel.objects.create(**validated_data,employee=employee)


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'employee_name', 'contact_number', 'email', 'postion', 'reporting_to', 'work_location'] 



class LeaveApplicationListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = LeaveApplicationModel
        fields = ['id','employee','apply_date','nature_of_leave','first_day','last_day','number_of_days','status']


    def to_representation(self, instance):
        rep = super(LeaveApplicationListSerializer, self).to_representation(instance)
        rep['employee'] = instance.employee.username
        return rep


class LeaveApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplicationModel
        fields = ['status']