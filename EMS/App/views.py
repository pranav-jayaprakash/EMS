from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class IndexView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        user = request.user


        if user.is_superuser == 1:


            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '------------':'-------------------------',
                'ACCESS' :'**Please login  && Verify Your Token..!**',
                '------':'-------------------------',
                'LOGIN PAGE' : 'http://127.0.0.1:8000/api/login/',
                'TOKEN GENERATION' : 'http://127.0.0.1:8000/api/token/',
                'TOKEN REFRESH' : 'http://127.0.0.1:8000/api/token/refresh/',
                'TOKEN VERIFICATION' : 'http://127.0.0.1:8000/api/token/verify/',
                ':::::::::::::::::::::::::':':::::::::::::::::::::::::',
                'CREATE EMPLOYEE' : 'http://127.0.0.1:8000/accounts/manager/employee-create/',
                'EMPLOYEE LIST':'http://127.0.0.1:8000/accounts/manager/employee-list/',
                'EMPLOYEE DETAILS' : 'http://127.0.0.1:8000/accounts/manager/employee-details/<id>/',
                '.......................':'...................................',
                'LEAVE APPLICATION LIST' : 'http://127.0.0.1:8000/accounts/manager/leave-application/list/',
                'LEAVE APPLICATION APPROVAL':'http://127.0.0.1:8000/accounts/manager/leave-application/details/<id>/',
                '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api/logout/'
                
            }
            return Response(content)

        else:

            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '------------':'-------------------------',
                'ACCESS' :'**Please login  && Verify Your Token..!**',
                '------':'-------------------------',
                'LOGIN PAGE' : 'http://127.0.0.1:8000/api/login/',
                'TOKEN GENERATION' : 'http://127.0.0.1:8000/api/token/',
                'TOKEN REFRESH' : 'http://127.0.0.1:8000/api/token/refresh/',
                'TOKEN VERIFICATION' : 'http://127.0.0.1:8000/api/token/verify/',
                ':::::::::::::::::::::::::':':::::::::::::::::::::::::',
                'CREATE LEAVE APPLICATION' : 'http://127.0.0.1:8000/accounts/employee/leave-applications/create/',
                'LEAVE APPLICATION LIST':'http://127.0.0.1:8000/accounts/employee/leave-application/',
                'LEAVE APPLICATION DETAILS' : 'http://127.0.0.1:8000/accounts/employee/leave-application/<id>/',
                '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api/logout/'
                
            }
            return Response(content)
