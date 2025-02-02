from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.
def student(request):
    return render(request, 'student/index.html')

#This is for Model Form
def addstudent(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Created Successfully.')
            # return HttpResponse("Student Created Successfully")
            return redirect('home')
    else:
        form = forms.StudentForm()
        
    return render(request, 'student/addstudent.html', {'form': form})

def student_list(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student) #filled up form with user data
    # form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Updated Successfully.')
            return redirect('home')
    return render(request, 'student/addstudent.html', {'form': form, 'edit': True})


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Deleted Successfully.')
    return redirect('home')

def details(request, id):
    student = models.Student.objects.get(id=id)
    return render(request, 'student/details.html', {'student': student})


    
# This is for HTML Form
# def addstudent(request):

#      if request.method == 'POST':
#          fname = request.POST.get('fname')
#          lname = request.POST.get('lname')
#          email = request.POST.get('email')
#          phone = request.POST.get('phone')
#          address = request.POST.get('address')
#          course = request.POST.get('course')
#          photo = request.FILES.get('photo')
         
#          student = models.Student(first_name=fname, last_name=lname, email=email, phone=phone, address=address, course=course, photo=photo )
#          #Object of a Student class
#          student.save() #data saved in student database
#          return HttpResponse("Student Created Successfully")
     
#      return render(request, 'student/addstudent.html')

