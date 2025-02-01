from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(request):
    return render(request, 'student/index.html')

def addstudent(request):
    return render(request, 'student/addstudent.html')