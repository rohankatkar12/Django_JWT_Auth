from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save

        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'email', 'established_at', 'address']


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'company', 'emp_salary']
        # depth = 2
        
    def create(self, validated_data):
        company_data = validated_data.pop('company')  # Extract company data
        company_instance, created = Company.objects.get_or_create(**company_data)
        
        employee_instance = Employee.objects.create(company=company_instance, **validated_data)
        return employee_instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()