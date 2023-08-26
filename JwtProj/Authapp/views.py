from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import *
from .serializers import *


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors})
        
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200, 'payload':serializer.data, 'message':'User Succesfully  Registerd'})


class LoginAPI(APIView):
    
    def post(self, request):
        try: 
            data = request.data
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                # print(username, password)
                user = authenticate(username = username, password = password)
                # print(user)
                if user is None:
                    return Response({'status':400, 'message':'invalid password', 'data':{}})
                
                refresh = RefreshToken.for_user(user)
                return Response({'status':200, 'payload':serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token)})

            return Response({'status':400, 'message':'something went wrong', 'error': serializer.errors})

        except Exception as e:
            print(e)






class EmployeeAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee_obj = Employee.objects.all()
        if employee_obj:
            serializer = EmployeeSerializer(employee_obj, many=True)
            response = {
                'status': 200,
                'payload':serializer.data
                        }
        else:
            response = {'status':500, 'message': 'No any record'}
        return Response(response)
    
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             response = {
                 'status': 200,
                 'message':'Data succesfully saved'
             }
        else:
            response = {
                 'status': 500,
                 'error': serializer.errors
             }
        return Response(response)


    def put(self, request):
        try:
            id = request.data['emp_id']
            emp_obj = Employee.objects.get(emp_id = id)
            serializer = EmployeeSerializer(emp_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200, 'message':'Data succesfully updated'})
            else:
                return Response({'status':403, 'error': serializer.errors})
        except Exception as e:
            return({'status':403, 'message':'invalid Employee Id'})
    
    
    def delete(self, request):
        try:
            id = request.GET.get('emp_id')
            emp_obj = Employee.objects.get(emp_id=id)
            emp_obj.delete()
            response = {'status':200, 'message':'Data Deleted Succesfully'}
            return Response(response)
        except Exception as e:
            return Response({'status':400, 'message':'Invalid Employee Id'})
        

