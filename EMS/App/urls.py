from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from App import views

urlpatterns = [
    path('', views.IndexView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)