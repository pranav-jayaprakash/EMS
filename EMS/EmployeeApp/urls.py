from EmployeeApp import views
from django.urls import path

urlpatterns=[
    path('leave-applications/create/',views.LeaveCreate.as_view()),
    path('leave-application/<int:pk>/',views.LeaveDetail.as_view()),
    path('leave-application/',views.LeaveList.as_view()),

] 