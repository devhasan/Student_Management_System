from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='home'),
    path('student/addstudent', views.addstudent, name='add_student'),
    path('student/edit/<int:id>/', views.update_student, name='update_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('student/details/<int:id>/', views.details, name='details'),
    

]