from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='RegisterUser'),
    path('employee/', EmployeeAPI.as_view(), name='EmployeeAPI'),
    path('login/', LoginAPI.as_view(), name='LoginAPI')
]
