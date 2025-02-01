from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('student/addstudent', views.addstudent, name='addstudent'),
]