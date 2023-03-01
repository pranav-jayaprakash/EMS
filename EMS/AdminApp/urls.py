from django.urls import path,re_path
from AdminApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('employee-create/', views.EmployeeCreate.as_view()),
    path('employee-list/', views.EmployeeList.as_view()),
    path('employee-details/<int:pk>/', views.EmployeeDetail.as_view()),

    path('leave-application/list/', views.LeaveApplicationList.as_view()),
    path('leave-application/details/<int:pk>/', views.LeaveApplicationUpdate.as_view()),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)